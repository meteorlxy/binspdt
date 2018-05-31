<template>
  <ElAside>
    <ElMenu
      :default-active="$route.path"
      :router="true">
      <ElMenuItem index="/">
        <i class="el-icon-setting"></i>{{ $t('routes.home') }}
      </ElMenuItem>

      <ElSubmenu index="1">
        <template slot="title"><i class="el-icon-news"></i>{{ $t('routes.binary') }}</template>

        <ElMenuItem index="/binary">{{ $t('routes.modules') }}</ElMenuItem>

        <!-- <ElMenuItemGroup> -->
          <!-- <template slot="title">分组一</template> -->
          <!-- <ElMenuItem index="/binary">{{ $t('routes.modules') }}</ElMenuItem> -->
        <!-- </ElMenuItemGroup> -->
      </ElSubmenu>

      <ElSubmenu index="2">
        <template slot="title"><i class="el-icon-document"></i>{{ $t('routes.source') }}</template>

        <ElMenuItemGroup>
          <!-- <template slot="title">分组一</template> -->
          <!-- <ElMenuItem index="/binary">{{ $t('routes.modules') }}</ElMenuItem> -->
        </ElMenuItemGroup>
      </ElSubmenu>
    </ElMenu>
  </ElAside>
</template>

<script>
export default {
  name: 'TheHomeAside'
}
</script>
