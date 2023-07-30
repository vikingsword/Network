import requests
from PIL import Image
from io import BytesIO


def get_captcha(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            print("Failed to get the captcha. Status code:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error occurred during request:", e)
        return None


if __name__ == "__main__":
    # 替换为目标网站的验证码URL
    captcha_url = "https://m.139w.com/IncFile/getcode.asp?rnd=1690425223592"

    captcha_image_data = get_captcha(captcha_url)

    if captcha_image_data:
        # 将图片数据转换为Image对象并显示
        image = Image.open(BytesIO(captcha_image_data))
        image.show()
    else:
        print("Failed to get the captcha image.")
