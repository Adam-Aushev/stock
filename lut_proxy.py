import os
local_filse = os.listdir()
if 'lut_proxy' not in local_filse:
    os.mkdir('lut_proxy')

os.system('nano video_links.txt')
with open('video_links.txt', 'r', encoding='utf-8') as link_file:
    link_file = link_file.readlines()

for link in link_file:
    if link_file:
        link = link.strip().strip('"').replace('\\', '/')
        print(link)
        link_split = link.split("/")
        
        for link_peace in reversed(link_split):
            if 'сони' not in link_peace.lower()   and 'коп' not in link_peace.lower()   and 'кенон' not in link_peace.lower()  and 'видео' not in link_peace.lower() :
                if link_peace != link_split[-1]:
                    dir_name = f'{link_peace}_{link_split[-1]}'
                else:
                    dir_name = link_peace
                break
        if dir_name not in os.listdir('lut_proxy'):
            os.mkdir(f'lut_proxy/{dir_name}')
        folder_files = os.listdir(link)
        lut_proxy_dir = os.listdir(f'lut_proxy/{dir_name}')
        video_list = ''
        for each_file in folder_files:
            if '.mp4' in each_file.lower() :
                end_name = f'{each_file[:each_file.rfind(".")]}_Proxy.mp4'
                print(end_name,  lut_proxy_dir)
                if end_name not in lut_proxy_dir:
                    code = (F'ffmpeg  -v error -i "{link}/{each_file}" -c:a aac -rf64 auto -c:v h264 -profile:v baseline -preset ultrafast  -pix_fmt yuv420p -crf 25 -vf scale=640:360,fps=25,lut3d="A7s_Cine_Filipp_Bloom.cube" -y "lut_proxy/{dir_name}/{end_name}"')            
                    os.system(code)
        #os.system("(for %i in (*.mp4) do @echo file '%i') > mylist.txt ")
        print(video_list)
print(f'{link}\\mylist.txt')