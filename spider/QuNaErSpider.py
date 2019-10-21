# coding=gbk
import pymysql
import time
db = pymysql.connect("129.204.193.180", "Lorin3", "8133xx", "datawarehouse")
cursor = db.cursor()
import requests
import json

list = [{'id': 627, 'name': '阿勒泰'}, {'id': 628, 'name': '阿里'}, {'id': 629, 'name': '安康'}, {'id': 630, 'name': '安庆'}, {'id': 631, 'name': '鞍山'}, {'id': 632, 'name': '安顺'}, {'id': 633, 'name': '安阳'}, {'id': 634, 'name': '白城'}, {'id': 635, 'name': '百色'}, {'id': 636, 'name': '白山'}, {'id': 637, 'name': '白银'}, {'id': 638, 'name': '保定'}, {'id': 639, 'name': '宝鸡'}, {'id': 640, 'name': '保山'}, {'id': 641, 'name': '包头'}, {'id': 642, 'name': '巴彦淖尔'}, {'id': 643, 'name': '巴音郭楞'}, {'id': 644, 'name': '巴中'}, {'id': 645, 'name': '北海'}, {'id': 646, 'name': '蚌埠'}, {'id': 647, 'name': '本溪'}, {'id': 648, 'name': '毕节'}, {'id': 649, 'name': '滨州'}, {'id': 650, 'name': '博尔塔拉'}, {'id': 651, 'name': '亳州'}, {'id': 652, 'name': '长春'}, {'id': 653, 'name': '长沙'}, {'id': 654, 'name': '成都'}, {'id': 655, 'name': '沧州'}, {'id': 656, 'name': '常德'}, {'id': 657, 'name': '昌都'}, {'id': 658, 'name': '昌吉'}, {'id': 659, 'name': '长治'}, {'id': 660, 'name': '常州'}, {'id': 661, 'name': '潮州'}, {'id': 662, 'name': '承德'}, {'id': 663, 'name': '郴州'}, {'id': 664, 'name': '赤峰'}, {'id': 665, 'name': '池州'}, {'id': 666, 'name': '崇左'}, {'id': 667, 'name': '楚雄'}, {'id': 668, 'name': '滁州'}, {'id': 669, 'name': '大理'}, {'id': 670, 'name': '大连'}, {'id': 671, 'name': '丹东'}, {'id': 672, 'name': '儋州'}, {'id': 673, 'name': '大庆'}, {'id': 674, 'name': '大同'}, {'id': 675, 'name': '大兴安岭'}, {'id': 676, 'name': '达州'}, {'id': 677, 'name': '德宏'}, {'id': 678, 'name': '德阳'}, {'id': 679, 'name': '定西'}, {'id': 680, 'name': '迪庆'}, {'id': 681, 'name': '东莞'}, {'id': 682, 'name': '东营'}, {'id': 683, 'name': '鄂尔多斯'}, {'id': 684, 'name': '恩施'}, {'id': 685, 'name': '鄂州'}, {'id': 686, 'name': '福州'}, {'id': 687, 'name': '佛山'}, {'id': 688, 'name': '抚顺'}, {'id': 689, 'name': '阜新'}, {'id': 690, 'name': '阜阳'}, {'id': 691, 'name': '抚州'}, {'id': 692, 'name': '广州'}, {'id': 693, 'name': '贵阳'}, {'id': 694, 'name': '甘南'}, {'id': 695, 'name': '赣州'}, {'id': 696, 'name': '广安'}, {'id': 697, 'name': '广元'}, {'id': 698, 'name': '桂林'}, {'id': 699, 'name': '固原'}, {'id': 700, 'name': '哈尔滨'}, {'id': 701, 'name': '海口'}, {'id': 702, 'name': '杭州'}, {'id': 703, 'name': '合肥'}, {'id': 704, 'name': '呼和浩特'}, {'id': 705, 'name': '哈密'}, {'id': 706, 'name': '邯郸'}, {'id': 707, 'name': '汉中'}, {'id': 708, 'name': '鹤壁'}, {'id': 709, 'name': '河池'}, {'id': 710, 'name': '鹤岗'}, {'id': 711, 'name': '黑河'}, {'id': 712, 'name': '衡水'}, {'id': 713, 'name': '衡阳'}, {'id': 714, 'name': '和田'}, {'id': 715, 'name': '河源'}, {'id': 716, 'name': '菏泽'}, {'id': 717, 'name': '贺州'}, {'id': 718, 'name': '红河'}, {'id': 719, 'name': '淮安'}, {'id': 720, 'name': '淮北'}, {'id': 721, 'name': '怀化'}, {'id': 722, 'name': '淮南'}, {'id': 723, 'name': '黄冈'}, {'id': 724, 'name': '黄山'}, {'id': 725, 'name': '黄石'}, {'id': 726, 'name': '惠州'}, {'id': 727, 'name': '葫芦岛'}, {'id': 728, 'name': '呼伦贝尔'}, {'id': 729, 'name': '湖州'}, {'id': 730, 'name': '济南'}, {'id': 731, 'name': '佳木斯'}, {'id': 732, 'name': '吉安'}, {'id': 733, 'name': '江门'}, {'id': 734, 'name': '焦作'}, {'id': 735, 'name': '嘉兴'}, {'id': 736, 'name': '嘉峪关'}, {'id': 737, 'name': '揭阳'}, {'id': 738, 'name': '金昌'}, {'id': 739, 'name': '晋城'}, {'id': 740, 'name': '景德镇'}, {'id': 741, 'name': '荆门'}, {'id': 742, 'name': '荆州'}, {'id': 743, 'name': '金华'}, {'id': 744, 'name': '济宁'}, {'id': 745, 'name': '晋中'}, {'id': 746, 'name': '锦州'}, {'id': 747, 'name': '九江'}, {'id': 748, 'name': '酒泉'}, {'id': 749, 'name': '鸡西'}, {'id': 750, 'name': '昆明'}, {'id': 751, 'name': '开封'}, {'id': 752, 'name': '喀什'}, {'id': 753, 'name': '克拉玛依'}, {'id': 754, 'name': '克孜勒苏柯尔克孜'}, {'id': 755, 'name': '兰州'}, {'id': 756, 'name': '拉萨'}, {'id': 757, 'name': '来宾'}, {'id': 758, 'name': '莱芜'}, {'id': 759, 'name': '廊坊'}, {'id': 760, 'name': '乐山'}, {'id': 761, 'name': '连云港'}, {'id': 762, 'name': '聊城'}, {'id': 763, 'name': '辽阳'}, {'id': 764, 'name': '辽源'}, {'id': 765, 'name': '丽江'}, {'id': 766, 'name': '临沧'}, {'id': 767, 'name': '临汾'}, {'id': 768, 'name': '临夏'}, {'id': 769, 'name': '临沂'}, {'id': 770, 'name': '林芝'}, {'id': 771, 'name': '丽水'}, {'id': 772, 'name': '六安'}, {'id': 773, 'name': '六盘水'}, {'id': 774, 'name': '柳州'}, {'id': 775, 'name': '陇南'}, {'id': 776, 'name': '龙岩'}, {'id': 777, 'name': '娄底'}, {'id': 778, 'name': '漯河'}, {'id': 779, 'name': '洛阳'}, {'id': 780, 'name': '泸州'}, {'id': 781, 'name': '吕梁'}, {'id': 782, 'name': '马鞍山'}, {'id': 783, 'name': '茂名'}, {'id': 784, 'name': '眉山'}, {'id': 785, 'name': '梅州'}, {'id': 786, 'name': '绵阳'}, {'id': 787, 'name': '牡丹江'}, {'id': 788, 'name': '南昌'}, {'id': 789, 'name': '南京'}, {'id': 790, 'name': '南宁'}, {'id': 791, 'name': '南充'}, {'id': 792, 'name': '南平'}, {'id': 793, 'name': '南通'}, {'id': 794, 'name': '南阳'}, {'id': 795, 'name': '那曲'}, {'id': 796, 'name': '内江'}, {'id': 797, 'name': '宁波'}, {'id': 798, 'name': '宁德'}, {'id': 799, 'name': '怒江'}, {'id': 800, 'name': '盘锦'}, {'id': 801, 'name': '攀枝花'}, {'id': 802, 'name': '平凉'}, {'id': 803, 'name': '萍乡'}, {'id': 804, 'name': '普洱'}, {'id': 805, 'name': '莆田'}, {'id': 806, 'name': '濮阳'}, {'id': 807, 'name': '黔东南'}, {'id': 808, 'name': '黔南'}, {'id': 809, 'name': '黔西南'}, {'id': 810, 'name': '青岛'}, {'id': 811, 'name': '庆阳'}, {'id': 812, 'name': '清远'}, {'id': 813, 'name': '秦皇岛'}, {'id': 814, 'name': '齐齐哈尔'}, {'id': 815, 'name': '七台河'}, {'id': 816, 'name': '泉州'}, {'id': 817, 'name': '曲靖'}, {'id': 818, 'name': '衢州'}, {'id': 819, 'name': '日喀则'}, {'id': 820, 'name': '日照'}, {'id': 821, 'name': '沈阳'}, {'id': 822, 'name': '石家庄'}, {'id': 823, 'name': '三门峡'}, {'id': 824, 'name': '三明'}, {'id': 825, 'name': '三沙'}, {'id': 826, 'name': '三亚'}, {'id': 827, 'name': '商洛'}, {'id': 828, 'name': '商丘'}, {'id': 829, 'name': '上饶'}, {'id': 830, 'name': '山南'}, {'id': 831, 'name': '汕头'}, {'id': 832, 'name': '汕尾'}, {'id': 833, 'name': '韶关'}, {'id': 834, 'name': '绍兴'}, {'id': 835, 'name': '邵阳'}, {'id': 836, 'name': '深圳'}, {'id': 837, 'name': '十堰'}, {'id': 838, 'name': '石嘴山'}, {'id': 839, 'name': '双鸭山'}, {'id': 840, 'name': '朔州'}, {'id': 841, 'name': '四平'}, {'id': 842, 'name': '松原'}, {'id': 843, 'name': '绥化'}, {'id': 844, 'name': '遂宁'}, {'id': 845, 'name': '随州'}, {'id': 846, 'name': '宿迁'}, {'id': 847, 'name': '宿州'}, {'id': 848, 'name': '苏州'}, {'id': 849, 'name': '太原'}, {'id': 850, 'name': '泰安'}, {'id': 851, 'name': '台州'}, {'id': 852, 'name': '泰州'}, {'id': 853, 'name': '唐山'}, {'id': 854, 'name': '天水'}, {'id': 855, 'name': '铁岭'}, {'id': 856, 'name': '铜川'}, {'id': 857, 'name': '通化'}, {'id': 858, 'name': '通辽'}, {'id': 859, 'name': '铜陵'}, {'id': 860, 'name': '铜仁'}, {'id': 861, 'name': '吐鲁番'}, {'id': 862, 'name': '武汉'}, {'id': 863, 'name': '乌鲁木齐'}, {'id': 864, 'name': '潍坊'}, {'id': 865, 'name': '威海'}, {'id': 866, 'name': '渭南'}, {'id': 867, 'name': '文山'}, {'id': 868, 'name': '温州'}, {'id': 869, 'name': '乌海'}, {'id': 870, 'name': '芜湖'}, {'id': 871, 'name': '乌兰察布'}, {'id': 872, 'name': '武威'}, {'id': 873, 'name': '无锡'}, {'id': 874, 'name': '吴忠'}, {'id': 875, 'name': '梧州'}, {'id': 876, 'name': '西安'}, {'id': 877, 'name': '西宁'}, {'id': 878, 'name': '厦门'}, {'id': 879, 'name': '湘潭'}, {'id': 880, 'name': '湘西'}, {'id': 881, 'name': '襄阳'}, {'id': 882, 'name': '咸宁'}, {'id': 883, 'name': '咸阳'}, {'id': 884, 'name': '孝感'}, {'id': 885, 'name': '邢台'}, {'id': 886, 'name': '新乡'}, {'id': 887, 'name': '信阳'}, {'id': 888, 'name': '新余'}, {'id': 889, 'name': '忻州'}, {'id': 890, 'name': '西双版纳'}, {'id': 891, 'name': '宣城'}, {'id': 892, 'name': '许昌'}, {'id': 893, 'name': '徐州'}, {'id': 894, 'name': '银川'}, {'id': 895, 'name': '雅安'}, {'id': 896, 'name': '延安'}, {'id': 897, 'name': '延边'}, {'id': 898, 'name': '盐城'}, {'id': 899, 'name': '阳江'}, {'id': 900, 'name': '阳泉'}, {'id': 901, 'name': '扬州'}, {'id': 902, 'name': '烟台'}, {'id': 903, 'name': '宜宾'}, {'id': 904, 'name': '宜昌'}, {'id': 905, 'name': '伊春'}, {'id': 906, 'name': '宜春'}, {'id': 907, 'name': '伊犁'}, {'id': 908, 'name': '伊犁哈萨克自治州'}, {'id': 909, 'name': '营口'}, {'id': 910, 'name': '鹰潭'}, {'id': 911, 'name': '益阳'}, {'id': 912, 'name': '永州'}, {'id': 913, 'name': '岳阳'}, {'id': 914, 'name': '玉林'}, {'id': 915, 'name': '榆林'}, {'id': 916, 'name': '运城'}, {'id': 917, 'name': '云浮'}, {'id': 918, 'name': '玉溪'}, {'id': 919, 'name': '郑州'}, {'id': 920, 'name': '枣庄'}, {'id': 921, 'name': '张家界'}, {'id': 922, 'name': '张家口'}, {'id': 923, 'name': '张掖'}, {'id': 924, 'name': '漳州'}, {'id': 925, 'name': '湛江'}, {'id': 926, 'name': '肇庆'}, {'id': 927, 'name': '昭通'}, {'id': 928, 'name': '镇江'}, {'id': 929, 'name': '中山'}, {'id': 930, 'name': '中卫'}, {'id': 931, 'name': '周口'}, {'id': 932, 'name': '舟山'}, {'id': 933, 'name': '珠海'}, {'id': 934, 'name': '驻马店'}, {'id': 935, 'name': '株洲'}, {'id': 936, 'name': '淄博'}, {'id': 937, 'name': '自贡'}, {'id': 938, 'name': '资阳'}, {'id': 939, 'name': '遵义'}, {'id': 940, 'name': '北京'}, {'id': 941, 'name': '上海'}, {'id': 942, 'name': '天津'}, {'id': 943, 'name': '重庆'}, {'id': 944, 'name': '香港'}, {'id': 945, 'name': '澳门'}]
# print(list)

headers = {
    "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Mobile Safari/537.36",
    "referer":"https://touch.dujia.qunar.com/list.qunar?dep=%E9%98%BF%E5%8B%92%E6%B3%B0&query=%E5%BC%A0%E5%AE%B6%E7%95%8C%E8%87%AA%E7%94%B1%E8%A1%8C&cfrom=zyx&it=pop_arrive_3"
}

url = "https://touch.dujia.qunar.com/list?modules=list,bookingInfo,activityDetail&dep={0}&query={1}自由行&type=all&dappDealTrace=true&cfrom=zyx&it=pop_arrive_more&date=&originQuery={1}自由行&page=home&orderby=sale-desc&ddf=true&needNoResult=true&originalquery={1}自由行&limit={2},20&includeAD=true&qsact=sort"

start = 0
total = 0

def getOne(comeFrom, to, start, total, fromId, toId):
    while True:
        response = requests.get(url.format(comeFrom, to, start), headers=headers)
        dt = json.loads(response.text)
        results = []
        try:
            if total == 0:
                total = int(dt["data"]["list"]["numFound"])
            results = dt["data"]["list"]["results"]
        except:
            start += 20
            if start > total - 20:
                break
            continue
        for i in results:
            people = 0
            price = 0
            try:
                people = i["soldCount"]
                price = i["price"]
            except:
                start += 20
                if start > total - 20:
                    break
                continue
            if people != 0:
                print("人数" + str(people))
                print("价格" + str(price))
                sql = """insert into infomations values(null, {}, {}, {}, {}, 10)""".format(fromId, toId, price, people)
                cursor.execute(sql)
                db.commit()
            else:
                print("没了")
                break
        start += 20
        if start > total - 20:
            break
        print("从" + comeFrom + "到" + to + "第" + str(start) + ", 共" + str(total))
        time.sleep(3)
# print(len(dt["data"]["list"]["results"]))
for city in list:
    getOne(city["name"], "桂林", 0, 0, city["id"], 698)
    time.sleep(5)

cursor.close()
db.close()