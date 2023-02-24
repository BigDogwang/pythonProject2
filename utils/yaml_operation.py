import yaml

class YamlOperation:
    #读取yaml文件
    @staticmethod       #静态方法
    def read_yaml(yamlpath,node_name):
        #yaml_path  yaml位置
        #node_name  获取对应的节点名称
        #return     列表，列表里包含的多个字典数据
        with open(yamlpath,'r',encoding='utf-8') as file:
            #安全加载文件流，获取yaml文件中的数据
            data = yaml.safe_load(file)
            print(data)
            dict = data[node_name]  #取出大字典中的 小字典
            print(list(dict.values()))  #.values是只取字典中的值
                                        #list()包裹住dict.values()，就是把这个值转化成列表
            return list(dict.values())  #返回数据

if __name__ == '__main__':
    YamlOperation.read_yaml('../data/data_tianqi.yaml','test_tianqi')