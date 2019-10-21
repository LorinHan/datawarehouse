<template>
  <div id="price">
      <menu class="leftMenu">
          <left-menu :getData="getData" :provinces="provinces" :type="'provinces'"></left-menu>
      </menu>
      <div class="main">
          <el-col style="text-align: right;padding-right: 50px;">
                <el-dropdown trigger="click" style="width: 100px;height: 35px;text-align: center;lineHeight: 35px;backgroundColor: #409eff;color: #fff;borderRadius: 3px;cursor: pointer;"  @command="changeCity">
                <span class="el-dropdown-link" style="display: block;width: 100%;">
                    {{choosed}}<i class="el-icon-arrow-down el-icon--right"></i>
                </span>
                <el-dropdown-menu slot="dropdown" style="height: 400px;overflow: auto;">
                    <el-dropdown-item v-for="item in touristList" :key="item.id" :command="item">{{item.city}}</el-dropdown-item>
                </el-dropdown-menu>
                </el-dropdown>
            </el-col>
            
          <div id="priceCounts" style="width: 100%;height: 760px;marginTop: 35px;"></div>
      </div>
  </div>
</template>

<script>
import LeftMenu from "@/components/LeftMenu";
export default {
    components: {LeftMenu},
    props: ["setLoading"],
    data() {
        return {
            provinces: [],
            touristId: 878,
            touristList: [],
            choosed: "",
            choosedProvince: {}
        }
    },
    methods: {
        changeCity(item) {
            this.choosed = item.city;
            this.touristId = item.city_id;
            this.getData(this.choosedProvince);
        },
        getData(province, minPrice, maxPrice) {
            let priceList = [{min: 0, max: 1000}, {min: 1000, max: 2500}, {min: 2500, max: 4000}, {min: 4000, max: 20000}];
            this.choosedProvince = province;
            let values = [];
             this.$ajax.get("/datawarehouse/provinceToTouristPrice?provinceId=" + province.id + "&touristId=" + this.touristId + "&minPrice=" + priceList[0].min + "&maxPrice=" + priceList[0].max).then(res => {
                this.$props.setLoading(true);
                let name = priceList[0].min + "到" + priceList[0].max + "元"
                values.push({name: name, value: res.data[0]["sum(inf.count)"]});
                this.$ajax.get("/datawarehouse/provinceToTouristPrice?provinceId=" + province.id + "&touristId=" + this.touristId + "&minPrice=" + priceList[1].min + "&maxPrice=" + priceList[1].max).then(res => {
                    let name = priceList[1].min + "到" + priceList[1].max + "元"
                    values.push({name: name, value: res.data[0]["sum(inf.count)"]});
                    this.$ajax.get("/datawarehouse/provinceToTouristPrice?provinceId=" + province.id + "&touristId=" + this.touristId + "&minPrice=" + priceList[2].min + "&maxPrice=" + priceList[2].max).then(res => {
                        let name = priceList[2].min + "到" + priceList[2].max + "元"
                        values.push({name: name, value: res.data[0]["sum(inf.count)"]});
                        this.$ajax.get("/datawarehouse/provinceToTouristPrice?provinceId=" + province.id + "&touristId=" + this.touristId + "&minPrice=" + priceList[3].min + "&maxPrice=" + priceList[3].max).then(res => {
                            this.$props.setLoading(false);
                            let name = priceList[3].min + "元以上"
                            values.push({name: name, value: res.data[0]["sum(inf.count)"]});
                            let myChart = echarts.init(document.getElementById('priceCounts'));
                            let option = {
                                title: {
                                    text: this.choosedProvince.province + "省到" + this.choosed + '价格信息',
                                    x:'center',
                                    textStyle: {color: "#000"}
                                },
                                tooltip: {
                                    trigger: 'item',
                                    formatter: "{a} <br/>{b}: {c} ({d}%)"
                                },
                                legend: {
                                    orient: 'vertical',
                                    x: 'left',
                                    data:['0到1000元','1000到2500元','2500到4000元','4000元以上']
                                },
                                series: [
                                    {
                                        name:'价格区间',
                                        type:'pie',
                                        radius: ['50%', '70%'],
                                        avoidLabelOverlap: true,
                                        label: {
                                            emphasis: {
                                                show: true,
                                                textStyle: {
                                                    fontSize: '30',
                                                    fontWeight: 'bold'
                                                }
                                            }
                                        },
                                        labelLine: {
                                            normal: {
                                                show: true
                                            }
                                        },
                                        data: values
                                    }
                                ]
                            };
                            myChart.setOption(option);
                            //建议加上以下这一行代码，不加的效果图如下（当浏览器窗口缩小的时候）。超过了div的界限（红色边框）
                            window.addEventListener('resize',function() {myChart.resize()});
                        });
                    });
                });
            });
        }
    },
    mounted() {
        this.$ajax.get("/datawarehouse/getAllTouristAttractions").then(res => {
            this.touristList = res.data;
            this.choosed = "厦门";
        })
        this.$ajax.get("/datawarehouse/getAllProvinces").then(res => {
            this.provinces = res.data;
        })
        let province = {id: 1, province: "河北"};
        this.getData(province, 0, 1000);
    }
}
</script>

<style lang="less" scoped>
    #price{
         .leftMenu{float: left;width: 14%;overflow: auto;height: 800px;}
         .main{
             width: 86%;
             height: 800px;
             float: left;
             background-color: #f0f0f0;
         }
    }
</style>