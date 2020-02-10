import unittest
from mydict import Dict

class TestDict(unittest.TestCase):
    # 运行每个'test_xx'之前执行setUp
    def setUp(self):
        print('setUp...')
        # print('setUp... %s' % getattr(self.setUp, '__name__'))
    # 运行每个'test_xx'之后执行tearDown
    def tearDown(self):
        print('teartDown...')
    def test_init(self):
        d = Dict(a=1, b='test')
        # 断言：期待相等
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        # 通过self.__setattr__生效的吧
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        # 断言：通过d['empty']访问key时、期待抛出raise(KeyError)
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == "__main__":
    # 运行以test_开头的方法 
    unittest.main()
