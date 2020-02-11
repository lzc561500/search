import yaml


class Data_key:

        def data_yml_read(self,path):
            with open("./data/%s"%path,"r",encoding="utf-8") as f:
                return yaml.load(f,Loader=yaml.FullLoader)

        def data_yml_key(self,path,key):
            return self.data_yml_read(path)[key]


# if __name__ == '__main__':
#     data=Data_key().data_yml_key("test.yml","test_login")
#     print(data)