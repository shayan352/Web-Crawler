import requests

def get_titles(url):
    try:
        response = requests.get(url)

        my_text = response.text

        with open("my_text.txt", mode="w", encoding="utf-8") as myfile:
            myfile.write(my_text)

        with open("my_text.txt", mode="r", encoding="utf-8") as myfile:
            my_text = myfile.read()

        titles = []

        my_start = 0

        while True:
            my_start = my_text.find('title="', my_start)

            if my_start == -1:
                break

            my_end = my_text.find('"', my_start + 7)

            if my_end == -1:
                break

            title = my_text[my_start + 7:my_end].strip()

            if (title.startswith("بیمارستان") or
                title.startswith("کلینیک") or
                title.startswith("درمانگاه") or
                title.startswith("آزمایشگاه") or
                title.startswith("مطب")):

                if title not in titles:
                    titles.append(title)

            my_start = my_end + 1

        return titles

    except:
        print("خطا در اتصال به سایت")
        return []


url = input("آدرس سایت را وارد کنید: ")

titles = get_titles(url)

print("تعداد مراکز:", len(titles))

for i in range(len(titles)):

    print(i + 1, ".", titles[i])