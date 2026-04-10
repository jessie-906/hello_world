def city_and_country(city,country,population=''):
    if population :
        full = f"{city},{country} - {population}"
        
    else:
        full = f"{city},{country}"
    return full.title()

def test_city_country():
    """能够正确处理地名和国家名称吗？"""
    formatted_name = city_and_country('santiago','chile')
    assert formatted_name == 'Santiago,Chile'
    #安装第三方包输入：E:\programme\python\python.exe -m pip install pytest(package_name)
    #测试指令输入：E:\programme\python\python.exe -m pytest test_code\test_city.py(文件路径)

def test_city_country_population():
    """能够正确处理地名和国家名称和人数吗？"""
    formatted_name = city_and_country('santiago','chile','5000000')
    assert formatted_name == 'Santiago,Chile - 5000000'