from gtts import gTTS
from playsound3 import playsound
import speech_recognition as sr
import sounddevice as sd
import tempfile
import os
import re

nhan_dang = sr.Recognizer()

GIONG_NOI = "vi-VN-HoaiMyNeural"


def noi(text):
    print("🤖:", text)

    with tempfile.NamedTemporaryFile(
        suffix=".mp3", delete=False
    ) as f:
        file = f.name

    try:
        tts = gTTS(text=text, lang="vi", slow=False)
        tts.save(file)

        playsound(file, block=True)

    except Exception as e:
        print("Lỗi TTS:", e)

    finally:
        if os.path.exists(file):
            os.remove(file)

def nghe():
    try:
        print("🎤 Đang nghe trong 6 giây...")

        # Ghi am 6 giay
        audio = sd.rec(
            16000 * 6,
            samplerate=16000,
            channels=1,
            dtype="int16"
        )
        sd.wait()

        du_lieu = sr.AudioData(
            audio.tobytes(),
            sample_rate=16000,
            sample_width=2
        )

        text = nhan_dang.recognize_google(
            du_lieu,
            language="vi-VN"
        )

        print("👤:", text)
        return text.lower()

    except sr.UnknownValueError:
        noi("Tôi không nghe rõ. Bạn nói lại nhé.")

    except sr.RequestError:
        noi("Không thể kết nối Google. Kiểm tra Internet.")
        raise SystemExit

    except Exception as e:
        print("Lỗi micro:", e)
        raise SystemExit

    return ""


def nhap_so(cau_hoi):
    while True:
        noi(cau_hoi)
        text = nghe()

        text = text.replace("phẩy", ".")
        text = text.replace("chấm", ".")
        text = text.replace(",", ".")

        text = re.sub(
            r"(\d+)\s*(?:mét|m)\s*(\d{1,2})",
            r"\1.\2",
            text
        )

        so = re.search(r"\d+(?:\.\d+)?", text)

        if so:
            gia_tri = float(so.group())

            if gia_tri > 0:
                return gia_tri

        noi("Tôi chưa nhận được số hợp lệ. Hãy nói lại.")


noi("Xin chào! Tôi là trợ lý tính chỉ số BMI.")

while True:
    can_nang = nhap_so(
        "Bạn nặng bao nhiêu ki lô gam?"
    )

    chieu_cao = nhap_so(
        "Bạn cao bao nhiêu xen ti mét?"
    )

    if chieu_cao > 3:
        chieu_cao = chieu_cao / 100

    bmi = can_nang / (chieu_cao ** 2)

    if bmi < 18.5:
        ket_qua = "Gầy"
    elif bmi < 25:
        ket_qua = "Bình thường"
    elif bmi < 30:
        ket_qua = "Thừa cân"
    else:
        ket_qua = "Béo phì"

    bmi = round(bmi, 2)

    print("\n===== KẾT QUẢ BMI =====")
    print("Cân nặng:", can_nang, "kg")
    print("Chiều cao:", chieu_cao, "m")
    print("BMI:", bmi)
    print("Phân loại:", ket_qua)
    print("======================\n")

    bmi_doc = str(bmi).replace(".", ",")

    noi("Chỉ số BMI của bạn là " + bmi_doc)
    noi("Bạn thuộc nhóm " + ket_qua)

    while True:
        noi("Bạn có muốn tính tiếp không?")
        tra_loi = nghe()

        if any(tu in tra_loi for tu in [
            "không", "thôi", "dừng", "thoát"
        ]):
            noi("Cảm ơn bạn đã sử dụng. Tạm biệt!")
            break

        elif any(tu in tra_loi for tu in [
            "có", "tiếp", "được", "ừ"
        ]):
            noi("Được rồi, chúng ta tiếp tục nhé!")
            break

        else:
            noi("Tôi chưa hiểu. Bạn hãy nói có hoặc không.")

    if any(tu in tra_loi for tu in [
        "không", "thôi", "dừng", "thoát"
    ]):
        break
