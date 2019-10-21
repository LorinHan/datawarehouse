<template>
  <div id="menu">
    <el-menu
      v-if="type == 'area'"
      default-active="1-2"
      class="leftMenu"
      @open="handleOpen"
      @close="handleClose"
      background-color="#363B41"
      text-color="#eee"
      active-text-color="#61E29F">
      <el-submenu :index="outindex + 1" v-for="(area, key, outindex) in touristList" :key="outindex">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>{{key | touristName}}</span>
        </template>
        <el-menu-item-group v-for="(city, index) in area" :key="index">
          <el-menu-item :index="(outindex + 1) + '-' + (index + 1)" @click="getData(city.city_id, city.city)">{{city.city}}</el-menu-item>
        </el-menu-item-group>
      </el-submenu>
    </el-menu>
    <el-menu
      v-if="type == 'provinces'"
      default-active="1-1"
      class="leftMenu"
      @open="handleOpen"
      @close="handleClose"
      background-color="#363B41"
      text-color="#eee"
      active-text-color="#61E29F">
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>所有省份</span>
        </template>
        <el-menu-item-group v-for="(item, index) in provinces" :key="index">
          <el-menu-item :index="'1-' + (index + 1)" @click="getData(item)">{{item.province}}</el-menu-item>
        </el-menu-item-group>
      </el-submenu>
    </el-menu>
  </div>
</template>

<script>
export default {
    props: ["touristList", "getData", "type", "provinces"],
    methods: {
      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      }
    },
    filters: {
      touristName(value) {
        switch(value) {
            case "huadong": return "华东地区";
            case "xinan": return "西南地区";
            case "xibei": return "西北地区";
            case "huabei": return "华北地区";
            case "dongbei": return "东北地区";
            case "huazhong": return "华中地区";
            case "huanan": return "华南地区";
        }
      }
    }
}
</script>

<style scoped lang="less">
    #menu{
        width: 100%;
        height:100%;
        .leftMenu{height: 100%;}
    }
</style>