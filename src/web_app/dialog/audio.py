from magic import Magic
from pydub import AudioSegment
from io import BytesIO


def audio_convert_to_wav(bytes_data):
    audio_format = Magic().from_buffer(bytes_data)
    if("webm" in audio_format.lower()):
        return audio_convert_webm_to_wav(bytes_data)
    elif("ogg" in audio_format.lower()):
        return audio_convert_ogg_to_wav(bytes_data)
    else:
        return None
    
def audio_convert_webm_to_wav(bytes_data):
    webm_audio = AudioSegment.from_file(BytesIO(bytes_data), format="webm")
    wav_audio = webm_audio.set_frame_rate(24000).set_channels(1).set_sample_width(2)
    wav_bytes = wav_audio.export(BytesIO(), format="wav").getvalue()
    return wav_bytes

def audio_convert_ogg_to_wav(bytes_data):
    ogg_audio = AudioSegment.from_file(BytesIO(bytes_data), format="ogg")
    wav_audio = ogg_audio.set_frame_rate(24000).set_channels(1).set_sample_width(2)
    wav_bytes = wav_audio.export(BytesIO(), format="wav").getvalue()
    return wav_bytes
    
