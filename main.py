import requests
from pathlib import Path
# ---------------------------------------------------------------------------------------
# ДЗ Задача 1

sh_list = ['Hulk', 'Captain America', 'Thanos']
# sh_list = ['Hulk', 'Captain America', 'Thanos', 'Ant-Man']
# sh_list = ['Hulk', 'Captain America']

def most_int_sh(sh_list):
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    # print(response.status_code)

    all_name_list = []
    all_int_list = []
    for _ in response.json():
        all_name_list.append(_['name'])
        all_int_list.append(_['powerstats']['intelligence'])
    all_sh_int_dict = dict(zip(all_name_list, all_int_list))
    # print(all_sh_int_dict)

    int_list = []
    for k in sh_list:
        int_list.append(all_sh_int_dict[k])
    # print(int_list)
    needed_int_dict = dict(zip(sh_list, int_list))
    # print(needed_int_dict)

    hundr_list = []
    for k, v in needed_int_dict.items():
        if v == 100:
            hundr_list.append(k)
    if len(hundr_list) <= 1:
        print(f'Самый умный из {len(sh_list)} супергероев {", ".join(needed_int_dict.keys())}: {max(needed_int_dict, key=needed_int_dict.get)}')
    else:
        print(f'Самый умный из {len(sh_list)} супергероев {", ".join(needed_int_dict.keys())}: {", ".join(hundr_list)}')

if __name__ == '__main__':
    most_int_sh(sh_list)


# ---------------------------------------------------------------------------------------
# ДЗ Задача 2 (загрузка одного файла)

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': '/' + file_path.split('/')[-1]}
        headers = {'Authorization': 'OAuth '+token}

        response = requests.get(url, headers=headers, params=params)

        print(response.status_code)
        if 200 <= response.status_code < 300:
            data = response.json()

            url = data['href']
            with open(Path(file_path), 'rb') as f:
                response = requests.put(url, files={'file': f})
                print(response.status_code)


if __name__ == '__main__':
    path_to_file = "C:/Users/Ksenia/Documents/quotes.txt"
    token = '...'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)


# ---------------------------------------------------------------------------------------
# ДЗ Задача 2 (загрузка файлов по списку из одной папки)

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, folder_path: str, files_list):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        for one in files_list:

            url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
            params = {'path': '/' + one}
            headers = {'Authorization': 'OAuth '+token}

            response = requests.get(url, headers=headers, params=params)

            print(response.status_code)
            if 200 <= response.status_code < 300:
                data = response.json()

                url = data['href']
                with open(Path(folder_path + '/' + one), 'rb') as f:
                    response = requests.put(url, files={'file': f})
                    print(response.status_code)


if __name__ == '__main__':
    path_to_folder = "C:/Users/Ksenia/Documents"
    file_list = ['quotes_1.txt', 'quotes_2.txt', 'quotes_3.txt']
    token = '...'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_folder, file_list)
