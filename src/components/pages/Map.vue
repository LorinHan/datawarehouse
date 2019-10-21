<template>
  <div id="map">
      <menu class="leftMenu">
          <left-menu :touristList="touristList" :getData="getData" :type="'area'"></left-menu>
      </menu>
      <div id="myChartChina" :style="{float: 'left', width: '86%', height: '800px'}"></div>
  </div>
</template>

<script>
import LeftMenu from "@/components/LeftMenu";
export default {
    components: {LeftMenu},
    props: ["setLoading"],
    data() {
        return {
            choosed_city: "",
            touristList: {}
        }
    },
    methods: {
        drawLine(provinceData) {
        // 基于准备好的dom，初始化echarts实例     
        
        var myChartChina = echarts.init(document.getElementById('myChartChina'));

             var geoCoordMap = {
                '黑龙江': [127.9688, 45.368],
                '内蒙古': [110.3467, 41.4899],
                "吉林": [125.8154, 44.2584],
                '北京市': [116.4551, 40.2539],
                "辽宁": [123.1238, 42.1216],
                "河北": [114.4995, 38.1006],
                "天津": [117.4219, 39.4189],
                "山西": [112.3352, 37.9413],
                "陕西": [109.1162, 34.2004],
                "甘肃": [103.5901, 36.3043],
                "宁夏": [106.3586, 38.1775],
                "青海": [101.4038, 36.8207],
                "新疆": [87.9236, 43.5883],
                "西藏": [91.11, 29.97],
                "四川": [103.9526, 30.7617],
                "重庆": [108.384366, 30.439702],
                "山东": [117.1582, 36.8701],
                "河南": [113.4668, 34.6234],
                "江苏": [118.8062, 31.9208],
                "安徽": [117.29, 32.0581],
                "湖北": [114.3896, 30.6628],
                "浙江": [119.5313, 29.8773],
                "福建": [119.4543, 25.9222],
                "江西": [116.0046, 28.6633],
                "湖南": [113.0823, 28.2568],
                "贵州": [106.6992, 26.7682],
                "云南": [102.9199, 25.4663],
                "广东": [113.12244, 23.009505],
                "广西": [108.479, 23.1152],
                "海南": [110.3893, 19.8516],
                '上海': [121.4648, 31.2891]
            };
     var chinaDatas = provinceData;
     var convertData = function(data) {
         var res = [];
         for (var i = 0; i < data.length; i++) {
             var geoCoord = geoCoordMap[data[i][0].name];
             if (geoCoord) {
                 res.push({
                     name: data[i][0].name,
                     value: geoCoord.concat(data[i][0].value)
                 });
             }
         }
         return res;
     };

     var option = {
         backgroundColor: '#3F4650',
         title: {
                    text: "全国各省到 " + this.choosed_city + " 旅游人数",
                    x:'center',
                    textStyle: {color: "#eee"}
                },
         visualMap: [{
             type: 'continuous',
             show: false,
             seriesIndex: 0,
             text: ['bar3D'],
             calculable: true,
             inRange: {
                 color: ['#87aa66', '#eba438', '#d94d4c']
             }
         }],
         geo3D: {
             map: 'china',
             roam: true,
             itemStyle: {
                 areaColor: '#000',
                 opacity: 1,
                 borderWidth: 0.8,
                 borderColor: 'rgb(62,215,213)'
             },
             label: {
                 show: false,
             },
             emphasis: { //当鼠标放上去  地区区域是否显示名称
                 label: {
                     show: true,
                     textStyle: {
                         color: '#fff',
                         fontSize: 3,
                         backgroundColor: 'rgba(0,23,11,0)'
                     }
                 }
             },
             light: {
                 main: {
                     color: '#fff', //光照颜色
                     intensity: 1.2, //光照强度
                     shadowQuality: 'high', //阴影亮度
                     shadow: true, //是否显示阴影
                     //                        alpha: 55,
                     beta: 10

                 },
                 ambient: {
                     intensity: 0.3
                 }
             },
             itemStyle: {//三维图形的视觉属性
                color:'rgb(5,101,123)',
                borderWidth:1,
                borderColor:'rgb(62,215,213)'
            },
         },
         series: [{
             name: 'bar3D',
             type: "bar3D",
             coordinateSystem: 'geo3D',
             barSize: 1, //柱子粗细
             shading: 'lambert',
             opacity: 0.1,
             label: {
                 show: false,
                 formatter: function(data) {
                     //                        console.log(data)
                     var res = data.name + " " + data.value[2]
                     return res
                 }
             },
             data: convertData(chinaDatas),
         }]
     }
        myChartChina.setOption(option);
        window.onresize=function(){
            // resizeMyChartContainer();
            myChartChina.resize();
        }
      },
      getData(cityId, cityName) {
          this.$props.setLoading(true);
          this.choosed_city = cityName;
          this.$ajax.get("/datawarehouse/getProvinceCountsByCityId?cityId=" + cityId).then(res => {
            let data = []
            res.data.forEach(item => {
                data.push([{name: item.province, value: item.count}]);
            });
            this.drawLine(data);
          this.$props.setLoading(false);
        })
      }
    },
    mounted() {
        this.$ajax.get("/datawarehouse/getAllTouristAttractions").then(res => {
            let touristList = {"huadong": [], "xinan": [], "xibei": [], "huabei": [], "dongbei": [], "huazhong": [], "huanan": []};
            res.data.forEach(item => {
                switch(item.area) {
                            case 1: touristList["huadong"].push(item);break;
                            case 2: touristList["xinan"].push(item);break;
                            case 3: touristList["xibei"].push(item);break;
                            case 4: touristList["huabei"].push(item);break;
                            case 5: touristList["dongbei"].push(item);break;
                            case 6: touristList["huazhong"].push(item);break;
                            case 7: touristList["huanan"].push(item);break;
                        }
            });
            this.touristList = touristList;
        })
        this.getData(878, "厦门");
    }
}
</script>

<style lang="less" scoped>
    #map{
        .leftMenu{float: left;width: 14%;overflow: auto;height: 800px;}
    }
</style>