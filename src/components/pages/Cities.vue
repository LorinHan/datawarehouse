<template>
  <div id="cities">
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
            
          <div id="eachCity" style="width: 100%;height: 760px;"></div>
      </div>
  </div>
</template>

<script>
import LeftMenu from "@/components/LeftMenu";
export default {
    components: {LeftMenu},
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
        getData(province) {
            this.choosedProvince = province;
            this.$ajax.get("/datawarehouse/getEachCityToSomeplaceCounts?provinceId=" + province.id + "&touristId=" + this.touristId).then(res => {
                let cities = [];
                let values = [];
                res.data.forEach(item => {
                    cities.push(item.city);
                    values.push(item.count);
                });
                let myChart = echarts.init(document.getElementById('eachCity'));
                var dataAxis = cities;
                var data = values;
                var dataShadow = [];
                let option = {
                    backgroundColor: '#3F4650',
                    title: {
                        text: this.choosedProvince.province + "省各市到" + this.choosed + '游客数量',
                        x:'center',
                        textStyle: {color: "#eee"}
                    },
                    yAxis: {
                        data: dataAxis,
                        axisLabel: {
                            inside: true,
                            textStyle: {
                                color: '#fff'
                            }
                        },
                        axisTick: {
                            show: false
                        },
                        axisLine: {
                            show: false
                        },
                        z: 10
                    },
                    xAxis: {
                        axisLine: {
                            show: false
                        },
                        axisTick: {
                            show: false
                        },
                        axisLabel: {
                            textStyle: {
                                color: '#999'
                            }
                        }
                    },
                    dataZoom: [
                        {
                            type: 'inside'
                        }
                    ],
                    series: [
                        { // For shadow
                            type: 'bar',
                            itemStyle: {
                                normal: {color: 'rgba(0,0,0,0.05)'}
                            },
                            barGap:'-100%',
                            barCategoryGap:'40%',
                            data: dataShadow
                        },
                        {
                            type: 'bar',
                            itemStyle: {
                                normal: {
                                    color: new echarts.graphic.LinearGradient(
                                        0, 0, 0, 1,
                                        [
                                            {offset: 0, color: '#83bff6'},
                                            {offset: 0.5, color: '#188df0'},
                                            {offset: 1, color: '#188df0'}
                                        ]
                                    )
                                },
                                emphasis: {
                                    color: new echarts.graphic.LinearGradient(
                                        0, 0, 0, 1,
                                        [
                                            {offset: 0, color: '#2378f7'},
                                            {offset: 0.7, color: '#2378f7'},
                                            {offset: 1, color: '#83bff6'}
                                        ]
                                    )
                                }
                            },
                            data: data
                        }
                    ]
                };
                
                myChart.setOption(option);
                //建议加上以下这一行代码，不加的效果图如下（当浏览器窗口缩小的时候）。超过了div的界限（红色边框）
                window.addEventListener('resize',function() {myChart.resize()});
            });
        },
        changeCity(item) {
            this.choosed = item.city;
            this.touristId = item.city_id;
            this.getData(this.choosedProvince);
        },
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
        this.getData(province);
    }
}
</script>

<style lang="less" scoped>
    #cities{
         .leftMenu{float: left;width: 14%;overflow: auto;height: 800px;}
         .main{
             width: 86%;
             height: 800px;
             float: left;
             background-color: #3F4650;
         }
    }
</style>