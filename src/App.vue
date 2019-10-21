<template>
  <div id="app">
    <div v-show="loading" style="position: absolute;width: 100%;height: 100%;z-index: 999;top: 0;left: 0;backgroundColor: #fff;opacity: .4;"><img style="position: relative; left: 42%;top: 35%;width: 250px;" src="/datawarehouse/static/loading.gif" alt=""></div>
    <header class="header">
          <div class="logo">
              <img src="/datawarehouse/static/logo.png" alt="" style="vertical-align: middle;width: 80px; height: 80px;">
          </div>
          <div class="center">
              <router-link to="/" class="item" active-class="active" exact>
                  <p class="ico iconfont icon-shouye"></p>
                  <p class="text">首页</p>
              </router-link>
              <router-link to="/map" class="item" active-class="active" exact>
                  <p class="ico iconfont icon-tupian"></p>
                  <p class="text">地图统计</p>
              </router-link>
              <router-link to="/cities" class="item" active-class="active" exact>
                  <p class="ico iconfont icon-tubiao"></p>
                  <p class="text">市级人数统计</p>
              </router-link>
              <router-link to="/price" class="item" active-class="active" exact>
                  <p class="ico iconfont icon-tishi"></p>
                  <p class="text">价格信息</p>
              </router-link>
          </div>
      </header>
    <router-view :setLoading="setLoading"/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      loading: false
    }
  },
  methods: {
    setLoading(val) {
      this.loading = val;
    }
  }
}
</script>

<style lang="less">
* {
  margin: 0;padding:0;box-sizing: border-box;
}
a{text-decoration: none;}
#app, html,  body{width:100%; height:100%;overflow: auto;}
#input{background-color: rgb(18, 42, 54);border-color: rgb(27, 50, 64);border-radius: 0; height: 55px;color: #fff;}
.header{
            width: 100%;
            height: 70px;
            background-color: #363B41;
            overflow: hidden;
            .logo{float: left; width: 14%;height: 100%;background-color: #363B41;text-align: center;line-height: 70px;}
            .center{
                float: left;width: 64%;height: 100%;
                .item{
                    height: 100%;
                    width: 10%;
                    float: left;
                    color: #ccc;
                    text-align: center;
                    margin-right: 10px;
                    transition: all .2s;
                    .ico{height: 40px; font-size: 24px;line-height: 40px;}
                    .text{height: 30px;line-height: 30px;font-size: 14px;}
                }
                .item:hover, .active{background-color: #3F4650;color: #fff;border-bottom: 4px solid #58E282;}
            }
            .right{float: right; width: 16%;height: 100%;line-height: 70px;text-align: center;padding: 0 20px;color: #eee;}
            .right > span:hover, .right > i:hover {color: #61E29F;}
        }
</style>
