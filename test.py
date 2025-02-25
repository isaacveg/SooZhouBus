import requests
import json
import logging
import time

#logging.basicConfig(level=logging.INFO, filename='./log.txt')
#logger = logging.getLogger(__name__)
#
def get_businfo(url, station):
    print('check~30s')
    #r   = requests.session()
    try:
        businfo = requests.get(url)
        businfo_json    = json.loads(businfo.text)
        businfo_std = businfo_json['data']['standInfo']
        #print(businfo_std)

        for i in businfo_std:
            if i not in station.keys():
                print(i+' '+businfo_std[i])

    except:
        print('error')
        
def get_businfo1(url, station):
    #print('check~30s')
    print(' ')
    businfo = requests.get(url)
    businfo_json    = json.loads(businfo.text)
    businfo_std = businfo_json['data']['standInfo']

    for i in businfo_std:
        if i not in station:
            print(i)
        else:
            print(station.index(i), end = ' ')
            
def target_req(url, station, target):
    
    businfo = requests.get(url)
    businfo_json    = json.loads(businfo.text)
    businfo_std = businfo_json['data']['standInfo']
    
    min = 40
    min_info    = {}
    for i in businfo_std:
        stat = station.index(i)  
        if (target-stat)>0 and (target-stat)<min :
            min = target-stat
            min_info    = businfo_std[i]
    
    print('closest bus length: '+ str(min))
    print('closest bus info:')
    for i in min_info:
        print(i)
                   
if __name__ == "__main__":
    url = 'https://szgj.2500.tv/api/v1/busline/bus?line_guid=0000000000LINELINEINFO18082357212871'
    station = {
'f1822311-fcae-4814-a4c6-d76a6de6489a': '独墅湖邻里中心公交首末站',
'4e0cc991-5c16-4c11-a66d-0e39f1d4af12': '独墅湖邻里中心北',
'd885bcc1-464f-4690-bd93-a0be648697c7': '独墅湖邻里中心东',
'e01d058c-05b7-44f9-8f28-4a8d01e5aea5': '菁英公寓',
'0f5786cf-0510-4609-bacf-682d98fd8e5c': '裕新路星湖街东',
'd34c1a39-c975-458f-96b2-41d1db78c80f': '腾飞创新园南',
'5434a25e-4aaa-4076-8792-a7fc7876acfe': '中科院药物所',
'965c32be-fdcf-6765-d909-242699d94ed3': '苏州评弹学校西',
'7d406579-a886-4027-a1d1-1cf82ab878ca': '苏州评弹学校北',
'c4a6f56d-009e-432d-a021-676243b3cb3e': '文萃广场',
'1b8c7113-4c03-48da-81c2-12d0b2096c2a': '文萃广场北',
'4fe71a7c-8bc2-4ea7-9391-d251fd558e9b': '文荟人才公寓',
'3ae7a609-9823-f4cd-efa0-f2a9f1155efd': '科教人才市场',
'5218795c-d577-2a62-3899-b8d1e8c7bc5b': '文荟广场西',
'b0f37eec-82da-b674-74ce-586ed3d78c20': '翰林邻里中心',
'750da97c-0dbe-4039-6999-b014e38d3480': '西交大',
'fa91958f-2a31-0f22-6d44-a30042350013': '南大研究生院',
'bbf2cbe1-4eb3-4701-bd93-12c21d6ffa28': '中国人民大学苏州校区',
'9d93c4c0-d65d-651d-5561-574eceacf7d4': '中科大.苏大独墅湖校区',
'fde93968-9f4e-4fb0-85d4-80fc230798ae': '中科大西②',
'c66fe9c1-2edc-4390-b32c-5b5040573a6b': '中科大西',
'8a1125bb-aa83-4746-870a-f9e3f4746052': '白鹭园北',
'7007ca1d-ef8f-4a5c-ab2a-79ee77d54786': '白鹭园南',
'8cae5251-9590-471f-b41c-27688d7da51f': '独墅湖体育馆北',
'96b37820-74e1-4a0e-933f-5fe68b68ab4b': '中科大西',
'd974fc75-fa91-b958-7366-396ccd387db0': '中科大.苏大独墅湖校区',
'06f96cac-fbe6-14b3-0a4f-9fd0e88f2d59': '中国人民大学苏州校区',
'bb0de81f-5bfd-485f-9d56-2af0467d8cf3': '南大研究生院',
'3df0c0de-009c-cf24-335c-de5aa5d7e4ea': '西交大  ',
'94da59d3-5dbc-4283-5e2d-c0be01465956': '翰林邻里中心',
'b16e8764-3eea-8cec-a870-37dfa1d87bdd': '文荟广场西',
'19420c4d-20e3-47ec-b3d4-205acf903dee': '科教人才市场',
'e4142035-c26e-44c3-bd24-dbc82ee88d03': '文荟人才公寓',
'203a6d11-9151-4b73-9db6-d729f461416a': '文萃广场',
'7ab30c1a-131f-4f1b-8b48-d69e033e1999': '苏州评弹学校北',
'c660d2ae-fe9c-ca78-6953-ee812d60400e': '苏州评弹学校西',
'f203c607-921e-4011-bdab-38f6b19f37b0': '中科院药物所',
'66033fb8-7a1f-4603-9920-0bd41c86e105': '腾飞创新园南',
'5f258981-e4ad-4aa3-adbb-ecb1220d14be': '裕新路星湖街东',
'1d0ca495-f1f2-4cef-8ad0-debc1a5d6538': '菁英公寓',
'43db2524-a553-4ea3-b6b6-49c8620541c4': '独墅湖学校',
'd91f5289-3b47-4699-a70e-5f7d79090e8a': '独墅湖邻里中心西',}

    station2    = ['f1822311-fcae-4814-a4c6-d76a6de6489a',
'4e0cc991-5c16-4c11-a66d-0e39f1d4af12',
'd885bcc1-464f-4690-bd93-a0be648697c7',
'e01d058c-05b7-44f9-8f28-4a8d01e5aea5',
'0f5786cf-0510-4609-bacf-682d98fd8e5c',
'd34c1a39-c975-458f-96b2-41d1db78c80f',
'5434a25e-4aaa-4076-8792-a7fc7876acfe',
'965c32be-fdcf-6765-d909-242699d94ed3',
'7d406579-a886-4027-a1d1-1cf82ab878ca',
'c4a6f56d-009e-432d-a021-676243b3cb3e',
'1b8c7113-4c03-48da-81c2-12d0b2096c2a',
'4fe71a7c-8bc2-4ea7-9391-d251fd558e9b',
'3ae7a609-9823-f4cd-efa0-f2a9f1155efd',
'5218795c-d577-2a62-3899-b8d1e8c7bc5b',
'b0f37eec-82da-b674-74ce-586ed3d78c20',
'750da97c-0dbe-4039-6999-b014e38d3480',
'fa91958f-2a31-0f22-6d44-a30042350013',
'bbf2cbe1-4eb3-4701-bd93-12c21d6ffa28',
'9d93c4c0-d65d-651d-5561-574eceacf7d4',
'fde93968-9f4e-4fb0-85d4-80fc230798ae',
'c66fe9c1-2edc-4390-b32c-5b5040573a6b',
'8a1125bb-aa83-4746-870a-f9e3f4746052',
'7007ca1d-ef8f-4a5c-ab2a-79ee77d54786',
'8cae5251-9590-471f-b41c-27688d7da51f',
'96b37820-74e1-4a0e-933f-5fe68b68ab4b',
'd974fc75-fa91-b958-7366-396ccd387db0',
'06f96cac-fbe6-14b3-0a4f-9fd0e88f2d59',
'bb0de81f-5bfd-485f-9d56-2af0467d8cf3',
'3df0c0de-009c-cf24-335c-de5aa5d7e4ea',
'94da59d3-5dbc-4283-5e2d-c0be01465956',
'b16e8764-3eea-8cec-a870-37dfa1d87bdd',
'19420c4d-20e3-47ec-b3d4-205acf903dee',
'e4142035-c26e-44c3-bd24-dbc82ee88d03',
'203a6d11-9151-4b73-9db6-d729f461416a',
'7ab30c1a-131f-4f1b-8b48-d69e033e1999',
'c660d2ae-fe9c-ca78-6953-ee812d60400e',
'f203c607-921e-4011-bdab-38f6b19f37b0',
'66033fb8-7a1f-4603-9920-0bd41c86e105',
'5f258981-e4ad-4aa3-adbb-ecb1220d14be',
'1d0ca495-f1f2-4cef-8ad0-debc1a5d6538',
'43db2524-a553-4ea3-b6b6-49c8620541c4',
'd91f5289-3b47-4699-a70e-5f7d79090e8a',]
    
    #while True:
    #    get_businfo1(url,station2)
    #    time.sleep(30)
    #   
    #target  = 24
    target  = 12
    target_req(url=url, station=station2, target=target) 
    
