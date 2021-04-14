# Autotesting for Dictionary Shopping Lab

import pytest

import Shopping

og_stock = Shopping.stock.copy()


class Test_Part1:
    def test_function_defined(self):
        assert getattr(Shopping, "buy_the_store", None) is not None, "You seem to not have defined a function named 'buy_the_store'?"

    def test_amount_returned(self):
        student = Shopping.buy_the_store(Shopping.stock, Shopping.prices)
        assert student == 216, "You are not returning the proper amount for buying the store!"

class Test_Part2:
    def test_function_defined(self):
        assert getattr(Shopping, "buy_list", None) is not None, "You seem to not have defined a function named 'buy_list'?"

    def test_mutate_stock_dict(self):
        student = Shopping.buy_list(Shopping.shopping_list_A, Shopping.stock, Shopping.prices)
        assert og_stock != Shopping.stock, "Did you mutate and change the stock dictionary? Because you should have!"

    def test_correct_single_amount(self):
        Shopping.stock = og_stock.copy()
        student = Shopping.buy_list(Shopping.shopping_list_B, Shopping.stock, Shopping.prices)
        if type(student)==tuple or type(student)==list:
            assert student[0] == 96
        else:
            assert student == 96

    def test_correct_chained_amounts(self): #36,70,77
        Shopping.stock = og_stock.copy()
        lists = [Shopping.shopping_list_A, Shopping.shopping_list_B, Shopping.shopping_list_C]
        amts = [36, 70, 77]
        for l,amt in zip(lists,amts):
            student = Shopping.buy_list(l, Shopping.stock, Shopping.prices)
            if type(student)==tuple or type(student)==list:
                assert student[0] == amt
            else:
                assert student == amt
