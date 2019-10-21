<template>
  <div id="home">
      <center class="main">
          <div class="sbStatus">
              <div class="item" style="background-color: #FFA304;">
                  <p style="background-color: #FFB73B;">省份数量</p>
                  <p style="font-size: 26px;line-height: 110px;">27省, 4直辖市, 2特区</p>
              </div>
              <div class="item" style="background-color: #8BBB51;">
                  <p style="background-color: #A4CA77;">城市数量</p>
                  <p style="font-size: 40px;line-height: 110px;">319</p>
              </div>
              <div class="item" style="background-color: #FC9175;">
                  <p style="background-color: #FDA994;">景点数量</p>
                  <p style="font-size: 40px;line-height: 110px;">28</p>
              </div>
              <div class="item" style="background-color: #73D0F7;">
                  <p style="background-color: #92DAF9;">旅游信息数据量</p>
                  <p style="font-size: 40px;line-height: 110px;">320.7万</p>
              </div>
          </div>
          <div id="chart_example"></div>
          <div id="chart_example2"></div>
      </center>
  </div>
</template>

<script>
// import LeftMenu from "@/components/LeftMenu";
export default {
    data() {
        return {
        }
    },
    methods: {
        getAreaCounts() {
            this.$ajax.get("/datawarehouse/getTouristCounts?groupBy=area").then(res => {
                let data = res.data;
                let areaCounts = []
                data.forEach(item => {
                    if(item.count) {
                        let dataObj = {};
                        switch(item.area) {
                            case 1: dataObj.name = "华东地区";break;
                            case 2: dataObj.name = "西南地区";break;
                            case 3: dataObj.name = "西北地区";break;
                            case 4: dataObj.name = "华北地区";break;
                            case 5: dataObj.name = "东北地区";break;
                            case 6: dataObj.name = "华中地区";break;
                            case 7: dataObj.name = "华南地区";break;
                        }
                        dataObj.value = item.count;
                        areaCounts.push(dataObj);
                    }
                });
                // 饼图
                let myChart2 = echarts.init(document.getElementById('chart_example2'));
                let option2 = {
                        backgroundColor: '#3F4650',
                        title : {
                            text: '国内各区域游客数量',
                            x:'center',
                            textStyle: {color: "#eee"}
                        },
                        tooltip : {
                            trigger: 'item',
                            formatter: "{a} <br/>{b} : {c} ({d}%)"
                        },
                        legend: {
                            orient: 'vertical',
                            left: 'left',
                            data: ['华东地区','西南地区', '西北地区', '华北地区', '东北地区', '华中地区', '华南地区'],
                            textStyle: {color: "#eee"}
                        },
                        series : [
                            {
                                name: '旅游人数',
                                type: 'pie',
                                radius : '55%',
                                center: ['50%', '60%'],
                                data: areaCounts,
                                label: {
                                    normal: {
                                        show: true,
                                        positions: "right",
                                        formatter: function(p) {
                                            return p.name + (p.value/10000).toFixed(1) + "万";
                                        },
                                    }
                                },
                                itemStyle: {
                                    emphasis: {
                                        shadowBlur: 10,
                                        shadowOffsetX: 0,
                                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                                        },
                                    normal:{
                                        color:function(params) {
                                        //自定义颜色
                                        var colorList = [          
                                                '#00FFFF', '#58E282', '#FF0000', 'pink', 'orange', '#c0c0c0', 'yellow'
                                            ];
                                            return colorList[params.dataIndex]
                                            }
                                    }
                                }
                            }
                        ]
                    };
                myChart2.setOption(option2);
                //建议加上以下这一行代码，不加的效果图如下（当浏览器窗口缩小的时候）。超过了div的界限（红色边框）
                window.addEventListener('resize',function() {myChart2.resize()});
            });
        },
        getEachTouristCounts() {
            this.$ajax.get("/datawarehouse/getTouristCounts?groupBy=each").then(res => {
                let resData = res.data;
                let cities = [];
                let values = [];
                resData.forEach(item => {
                    cities.unshift(item.city);
                    if(!item.count) {item.count = 0;}
                    values.unshift(item.count);
                });

                let myChart = echarts.init(document.getElementById('chart_example'));
            var dataAxis = cities;
            var data = values;
            var dataShadow = [];

            // for (var i = 0; i < data.length; i++) {
            //     dataShadow.push(yMax);
            // }

            let option = {
                backgroundColor: '#3F4650',
                title: {
                    text: '各景点游客数量',
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
            })
        }
    },
    mounted() {
      this.getAreaCounts();
      this.getEachTouristCounts();
    }
}
</script>

<style scoped lang="less">
    #home{
        height: 100%;
        border-radius: 2%;
        .main{
            float:left;width: 100%;height: 800px;background-color: #363B41;
            .sbStatus{
                width: 100%;
                height: 200px;
                padding: 20px 1%;
                margin-bottom: 10px;
                .item{width: 21%;height: 100%;float: left;margin: 0 2%;border-radius: 10px;overflow: hidden;color: #fff;}
                .item > p:first-child{height: 25%;text-align: center;line-height: 40px;color: #f0f0f0;font-size: 18px;font-weight: 600;}
            }
            #chart_example{
                width: 65%;
                height: 800px;
                float: left;
            }
            #chart_example2{
                width: 35%;
                height: 800px;
                float: right;
            }
        }
    }
</style>