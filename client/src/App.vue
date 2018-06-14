<template>
  <div id="app">
    <ElContainer direction="vertical">
      <TheHeader/>

      <transition
        name="el-fade-in-linear"
        mode="out-in">
        <router-view class="main-container"/>
      </transition>
    </ElContainer>
  </div>
</template>

<script>
import TheHeader from '@/components/layouts/TheHeader'
export default {
  name: 'App',
  components: {
    TheHeader
  }
}
</script>

<style lang="scss">
html, body {
  margin: 0;
  padding: 0;
  height: 100%;
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  #app {
    height: 100%;
    .el-container {
      height: 100%;
    }
  }
}

hr {
  display: block;
  height: 1px;
  border: 0;
  border-top: 1px solid #eaecef;
  margin: 1.2rem 0;
  padding: 0;
}

.text-center {
  text-align: center;
}

.text-right {
  text-align: right;
}

.el-aside {
  height: 100%;
  .el-menu {
    height: 100%;
  }
}

.hint {
  color: #999;
}

.table-tools {
  margin-bottom: 15px;
}

.el-form.table-details {
  font-size: 0;
  .details-section {
    min-height: 80px;
  }
  .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
    .el-form-item__label {
      width: 100px;
      color: #99a9bf;
    }
    &.long {
      width: 100%;
    }
    &.details {
      label {
        width: 150px;
      }
    }
  }
}
</style>
