import requests,unittest

class Test_kuaidi(unittest.TestCase):
    """docstring for Test_kuaidi"""
    def setUp(self) :
        self.headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:46.0) Gecko/20100101 Firefox/46.0"
        }

    def chaxun_kuaidi(self,url,danhao,kd,kd_name):
        """
        '三个参数：单号、快递名称（拼音）、快递中文名
       如：
       danhao = '1202247993797'
       kd = 'yunda'
       kd_name = u"韵达快递"

        """
        #danhao = "1202247993797"
        #kd = "yunda" 
        # 这里对url的单号参数了
        url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html" %(danhao,kd)
        print(self.url)
        # 第一步发请求
        r = requests.get(self.url,headers=headers,verify=False)
        result = r.json()
        # 第二步获取结果 
        print(result['company'])    # 获取公司名称
        data = result["data"]   # 获取data里面内容
        print(data[0])      # 获取data里最上面有个
        get_result = data[0]['context']     # 获取已签收状态
        print(get_result)
        # 断言：测试结果与期望结果对比
        self.assertEqual(kd_name,result['company'])
        self.assertIn("已签收",get_result)

    def test_yunda(self):
        danhao='1202247993797'
        kd_name='韵达快递'
        kd = 'yunda'
        self.chaxun_kuaidi(danhao,kd,kd_name)

    def test_tiantian(self):
        danhao = '560697415000'
        kd = 'tiantian'
        kd_name = '天天快递'
        self.chaxun_kuaidi(danhao,kd,kd_name)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
    # #构建测试用例集
    # suite = unittest.TestSuite()
    # suite.addTest(Test_kuaidi('test_yunda'))
    # suite.addTest(Test_kuaidi('test_tiantian'))
    # #执行测试
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    