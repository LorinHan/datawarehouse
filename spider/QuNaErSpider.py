# coding=gbk
import pymysql
import time
db = pymysql.connect("129.204.193.180", "Lorin3", "8133xx", "datawarehouse")
cursor = db.cursor()
import requests
import json

list = [{'id': 627, 'name': '����̩'}, {'id': 628, 'name': '����'}, {'id': 629, 'name': '����'}, {'id': 630, 'name': '����'}, {'id': 631, 'name': '��ɽ'}, {'id': 632, 'name': '��˳'}, {'id': 633, 'name': '����'}, {'id': 634, 'name': '�׳�'}, {'id': 635, 'name': '��ɫ'}, {'id': 636, 'name': '��ɽ'}, {'id': 637, 'name': '����'}, {'id': 638, 'name': '����'}, {'id': 639, 'name': '����'}, {'id': 640, 'name': '��ɽ'}, {'id': 641, 'name': '��ͷ'}, {'id': 642, 'name': '�����׶�'}, {'id': 643, 'name': '��������'}, {'id': 644, 'name': '����'}, {'id': 645, 'name': '����'}, {'id': 646, 'name': '����'}, {'id': 647, 'name': '��Ϫ'}, {'id': 648, 'name': '�Ͻ�'}, {'id': 649, 'name': '����'}, {'id': 650, 'name': '��������'}, {'id': 651, 'name': '����'}, {'id': 652, 'name': '����'}, {'id': 653, 'name': '��ɳ'}, {'id': 654, 'name': '�ɶ�'}, {'id': 655, 'name': '����'}, {'id': 656, 'name': '����'}, {'id': 657, 'name': '����'}, {'id': 658, 'name': '����'}, {'id': 659, 'name': '����'}, {'id': 660, 'name': '����'}, {'id': 661, 'name': '����'}, {'id': 662, 'name': '�е�'}, {'id': 663, 'name': '����'}, {'id': 664, 'name': '���'}, {'id': 665, 'name': '����'}, {'id': 666, 'name': '����'}, {'id': 667, 'name': '����'}, {'id': 668, 'name': '����'}, {'id': 669, 'name': '����'}, {'id': 670, 'name': '����'}, {'id': 671, 'name': '����'}, {'id': 672, 'name': '����'}, {'id': 673, 'name': '����'}, {'id': 674, 'name': '��ͬ'}, {'id': 675, 'name': '���˰���'}, {'id': 676, 'name': '����'}, {'id': 677, 'name': '�º�'}, {'id': 678, 'name': '����'}, {'id': 679, 'name': '����'}, {'id': 680, 'name': '����'}, {'id': 681, 'name': '��ݸ'}, {'id': 682, 'name': '��Ӫ'}, {'id': 683, 'name': '������˹'}, {'id': 684, 'name': '��ʩ'}, {'id': 685, 'name': '����'}, {'id': 686, 'name': '����'}, {'id': 687, 'name': '��ɽ'}, {'id': 688, 'name': '��˳'}, {'id': 689, 'name': '����'}, {'id': 690, 'name': '����'}, {'id': 691, 'name': '����'}, {'id': 692, 'name': '����'}, {'id': 693, 'name': '����'}, {'id': 694, 'name': '����'}, {'id': 695, 'name': '����'}, {'id': 696, 'name': '�㰲'}, {'id': 697, 'name': '��Ԫ'}, {'id': 698, 'name': '����'}, {'id': 699, 'name': '��ԭ'}, {'id': 700, 'name': '������'}, {'id': 701, 'name': '����'}, {'id': 702, 'name': '����'}, {'id': 703, 'name': '�Ϸ�'}, {'id': 704, 'name': '���ͺ���'}, {'id': 705, 'name': '����'}, {'id': 706, 'name': '����'}, {'id': 707, 'name': '����'}, {'id': 708, 'name': '�ױ�'}, {'id': 709, 'name': '�ӳ�'}, {'id': 710, 'name': '�׸�'}, {'id': 711, 'name': '�ں�'}, {'id': 712, 'name': '��ˮ'}, {'id': 713, 'name': '����'}, {'id': 714, 'name': '����'}, {'id': 715, 'name': '��Դ'}, {'id': 716, 'name': '����'}, {'id': 717, 'name': '����'}, {'id': 718, 'name': '���'}, {'id': 719, 'name': '����'}, {'id': 720, 'name': '����'}, {'id': 721, 'name': '����'}, {'id': 722, 'name': '����'}, {'id': 723, 'name': '�Ƹ�'}, {'id': 724, 'name': '��ɽ'}, {'id': 725, 'name': '��ʯ'}, {'id': 726, 'name': '����'}, {'id': 727, 'name': '��«��'}, {'id': 728, 'name': '���ױ���'}, {'id': 729, 'name': '����'}, {'id': 730, 'name': '����'}, {'id': 731, 'name': '��ľ˹'}, {'id': 732, 'name': '����'}, {'id': 733, 'name': '����'}, {'id': 734, 'name': '����'}, {'id': 735, 'name': '����'}, {'id': 736, 'name': '������'}, {'id': 737, 'name': '����'}, {'id': 738, 'name': '���'}, {'id': 739, 'name': '����'}, {'id': 740, 'name': '������'}, {'id': 741, 'name': '����'}, {'id': 742, 'name': '����'}, {'id': 743, 'name': '��'}, {'id': 744, 'name': '����'}, {'id': 745, 'name': '����'}, {'id': 746, 'name': '����'}, {'id': 747, 'name': '�Ž�'}, {'id': 748, 'name': '��Ȫ'}, {'id': 749, 'name': '����'}, {'id': 750, 'name': '����'}, {'id': 751, 'name': '����'}, {'id': 752, 'name': '��ʲ'}, {'id': 753, 'name': '��������'}, {'id': 754, 'name': '�������տ¶�����'}, {'id': 755, 'name': '����'}, {'id': 756, 'name': '����'}, {'id': 757, 'name': '����'}, {'id': 758, 'name': '����'}, {'id': 759, 'name': '�ȷ�'}, {'id': 760, 'name': '��ɽ'}, {'id': 761, 'name': '���Ƹ�'}, {'id': 762, 'name': '�ĳ�'}, {'id': 763, 'name': '����'}, {'id': 764, 'name': '��Դ'}, {'id': 765, 'name': '����'}, {'id': 766, 'name': '�ٲ�'}, {'id': 767, 'name': '�ٷ�'}, {'id': 768, 'name': '����'}, {'id': 769, 'name': '����'}, {'id': 770, 'name': '��֥'}, {'id': 771, 'name': '��ˮ'}, {'id': 772, 'name': '����'}, {'id': 773, 'name': '����ˮ'}, {'id': 774, 'name': '����'}, {'id': 775, 'name': '¤��'}, {'id': 776, 'name': '����'}, {'id': 777, 'name': '¦��'}, {'id': 778, 'name': '���'}, {'id': 779, 'name': '����'}, {'id': 780, 'name': '����'}, {'id': 781, 'name': '����'}, {'id': 782, 'name': '��ɽ'}, {'id': 783, 'name': 'ï��'}, {'id': 784, 'name': 'üɽ'}, {'id': 785, 'name': '÷��'}, {'id': 786, 'name': '����'}, {'id': 787, 'name': 'ĵ����'}, {'id': 788, 'name': '�ϲ�'}, {'id': 789, 'name': '�Ͼ�'}, {'id': 790, 'name': '����'}, {'id': 791, 'name': '�ϳ�'}, {'id': 792, 'name': '��ƽ'}, {'id': 793, 'name': '��ͨ'}, {'id': 794, 'name': '����'}, {'id': 795, 'name': '����'}, {'id': 796, 'name': '�ڽ�'}, {'id': 797, 'name': '����'}, {'id': 798, 'name': '����'}, {'id': 799, 'name': 'ŭ��'}, {'id': 800, 'name': '�̽�'}, {'id': 801, 'name': '��֦��'}, {'id': 802, 'name': 'ƽ��'}, {'id': 803, 'name': 'Ƽ��'}, {'id': 804, 'name': '�ն�'}, {'id': 805, 'name': '����'}, {'id': 806, 'name': '���'}, {'id': 807, 'name': 'ǭ����'}, {'id': 808, 'name': 'ǭ��'}, {'id': 809, 'name': 'ǭ����'}, {'id': 810, 'name': '�ൺ'}, {'id': 811, 'name': '����'}, {'id': 812, 'name': '��Զ'}, {'id': 813, 'name': '�ػʵ�'}, {'id': 814, 'name': '�������'}, {'id': 815, 'name': '��̨��'}, {'id': 816, 'name': 'Ȫ��'}, {'id': 817, 'name': '����'}, {'id': 818, 'name': '����'}, {'id': 819, 'name': '�տ���'}, {'id': 820, 'name': '����'}, {'id': 821, 'name': '����'}, {'id': 822, 'name': 'ʯ��ׯ'}, {'id': 823, 'name': '����Ͽ'}, {'id': 824, 'name': '����'}, {'id': 825, 'name': '��ɳ'}, {'id': 826, 'name': '����'}, {'id': 827, 'name': '����'}, {'id': 828, 'name': '����'}, {'id': 829, 'name': '����'}, {'id': 830, 'name': 'ɽ��'}, {'id': 831, 'name': '��ͷ'}, {'id': 832, 'name': '��β'}, {'id': 833, 'name': '�ع�'}, {'id': 834, 'name': '����'}, {'id': 835, 'name': '����'}, {'id': 836, 'name': '����'}, {'id': 837, 'name': 'ʮ��'}, {'id': 838, 'name': 'ʯ��ɽ'}, {'id': 839, 'name': '˫Ѽɽ'}, {'id': 840, 'name': '˷��'}, {'id': 841, 'name': '��ƽ'}, {'id': 842, 'name': '��ԭ'}, {'id': 843, 'name': '�绯'}, {'id': 844, 'name': '����'}, {'id': 845, 'name': '����'}, {'id': 846, 'name': '��Ǩ'}, {'id': 847, 'name': '����'}, {'id': 848, 'name': '����'}, {'id': 849, 'name': '̫ԭ'}, {'id': 850, 'name': '̩��'}, {'id': 851, 'name': '̨��'}, {'id': 852, 'name': '̩��'}, {'id': 853, 'name': '��ɽ'}, {'id': 854, 'name': '��ˮ'}, {'id': 855, 'name': '����'}, {'id': 856, 'name': 'ͭ��'}, {'id': 857, 'name': 'ͨ��'}, {'id': 858, 'name': 'ͨ��'}, {'id': 859, 'name': 'ͭ��'}, {'id': 860, 'name': 'ͭ��'}, {'id': 861, 'name': '��³��'}, {'id': 862, 'name': '�人'}, {'id': 863, 'name': '��³ľ��'}, {'id': 864, 'name': 'Ϋ��'}, {'id': 865, 'name': '����'}, {'id': 866, 'name': 'μ��'}, {'id': 867, 'name': '��ɽ'}, {'id': 868, 'name': '����'}, {'id': 869, 'name': '�ں�'}, {'id': 870, 'name': '�ߺ�'}, {'id': 871, 'name': '�����첼'}, {'id': 872, 'name': '����'}, {'id': 873, 'name': '����'}, {'id': 874, 'name': '����'}, {'id': 875, 'name': '����'}, {'id': 876, 'name': '����'}, {'id': 877, 'name': '����'}, {'id': 878, 'name': '����'}, {'id': 879, 'name': '��̶'}, {'id': 880, 'name': '����'}, {'id': 881, 'name': '����'}, {'id': 882, 'name': '����'}, {'id': 883, 'name': '����'}, {'id': 884, 'name': 'Т��'}, {'id': 885, 'name': '��̨'}, {'id': 886, 'name': '����'}, {'id': 887, 'name': '����'}, {'id': 888, 'name': '����'}, {'id': 889, 'name': '����'}, {'id': 890, 'name': '��˫����'}, {'id': 891, 'name': '����'}, {'id': 892, 'name': '���'}, {'id': 893, 'name': '����'}, {'id': 894, 'name': '����'}, {'id': 895, 'name': '�Ű�'}, {'id': 896, 'name': '�Ӱ�'}, {'id': 897, 'name': '�ӱ�'}, {'id': 898, 'name': '�γ�'}, {'id': 899, 'name': '����'}, {'id': 900, 'name': '��Ȫ'}, {'id': 901, 'name': '����'}, {'id': 902, 'name': '��̨'}, {'id': 903, 'name': '�˱�'}, {'id': 904, 'name': '�˲�'}, {'id': 905, 'name': '����'}, {'id': 906, 'name': '�˴�'}, {'id': 907, 'name': '����'}, {'id': 908, 'name': '���������������'}, {'id': 909, 'name': 'Ӫ��'}, {'id': 910, 'name': 'ӥ̶'}, {'id': 911, 'name': '����'}, {'id': 912, 'name': '����'}, {'id': 913, 'name': '����'}, {'id': 914, 'name': '����'}, {'id': 915, 'name': '����'}, {'id': 916, 'name': '�˳�'}, {'id': 917, 'name': '�Ƹ�'}, {'id': 918, 'name': '��Ϫ'}, {'id': 919, 'name': '֣��'}, {'id': 920, 'name': '��ׯ'}, {'id': 921, 'name': '�żҽ�'}, {'id': 922, 'name': '�żҿ�'}, {'id': 923, 'name': '��Ҵ'}, {'id': 924, 'name': '����'}, {'id': 925, 'name': 'տ��'}, {'id': 926, 'name': '����'}, {'id': 927, 'name': '��ͨ'}, {'id': 928, 'name': '��'}, {'id': 929, 'name': '��ɽ'}, {'id': 930, 'name': '����'}, {'id': 931, 'name': '�ܿ�'}, {'id': 932, 'name': '��ɽ'}, {'id': 933, 'name': '�麣'}, {'id': 934, 'name': 'פ���'}, {'id': 935, 'name': '����'}, {'id': 936, 'name': '�Ͳ�'}, {'id': 937, 'name': '�Թ�'}, {'id': 938, 'name': '����'}, {'id': 939, 'name': '����'}, {'id': 940, 'name': '����'}, {'id': 941, 'name': '�Ϻ�'}, {'id': 942, 'name': '���'}, {'id': 943, 'name': '����'}, {'id': 944, 'name': '���'}, {'id': 945, 'name': '����'}]
# print(list)

headers = {
    "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Mobile Safari/537.36",
    "referer":"https://touch.dujia.qunar.com/list.qunar?dep=%E9%98%BF%E5%8B%92%E6%B3%B0&query=%E5%BC%A0%E5%AE%B6%E7%95%8C%E8%87%AA%E7%94%B1%E8%A1%8C&cfrom=zyx&it=pop_arrive_3"
}

url = "https://touch.dujia.qunar.com/list?modules=list,bookingInfo,activityDetail&dep={0}&query={1}������&type=all&dappDealTrace=true&cfrom=zyx&it=pop_arrive_more&date=&originQuery={1}������&page=home&orderby=sale-desc&ddf=true&needNoResult=true&originalquery={1}������&limit={2},20&includeAD=true&qsact=sort"

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
                print("����" + str(people))
                print("�۸�" + str(price))
                sql = """insert into infomations values(null, {}, {}, {}, {}, 10)""".format(fromId, toId, price, people)
                cursor.execute(sql)
                db.commit()
            else:
                print("û��")
                break
        start += 20
        if start > total - 20:
            break
        print("��" + comeFrom + "��" + to + "��" + str(start) + ", ��" + str(total))
        time.sleep(3)
# print(len(dt["data"]["list"]["results"]))
for city in list:
    getOne(city["name"], "����", 0, 0, city["id"], 698)
    time.sleep(5)

cursor.close()
db.close()