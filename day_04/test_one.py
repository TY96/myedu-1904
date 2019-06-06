import allure
@allure.feature('订单模块')
class Test_order:
    @allure.story('下订单')
    def test_order_add(self):
        assert '200' in 'cood = 200'
    @allure.story('取消订单')
    def test_order_wh(self):
        assert '404' in 'cood = 200'