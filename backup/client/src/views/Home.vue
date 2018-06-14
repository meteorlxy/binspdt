<template>
  <ElContainer>
    <TheHomeAside/>

    <ElMain>
      <h1 class="welcome">{{ $t('home.welcome') }}</h1>
      <p class="fullname">{{ $t('home.fullname') }}</p>
      <hr>

      <ElForm>
        <ElFormItem :label="$t('home.lang')">
          <ElSelect v-model="$i18n.locale">
            <ElOption label="English" value="en"/>
            <ElOption label="中文" value="zh"/>
          </ElSelect>
        </ElFormItem>
      </ElForm>
    </ElMain>
  </ElContainer>
</template>

<script>
import TheHomeAside from '@/components/layouts/TheHomeAside'
export default {
  name: 'Home',
  components: {
    TheHomeAside
  }
}
</script>

<style lang="scss" scoped>
.welcome {
  font-size: 1.5rem;
}
.fullname {
  color: #717379;
}
</style>
