from base.base_xpath import Xpath


if __name__ == '__main__':
    loc=["text,设置","index,1,1"]
    data=Xpath().make_xpath_with_feature(loc)
    print(data)