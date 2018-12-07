<template>
  <MainFooter>
    <div class="float-right d-none d-sm-block-down">
      Binary Software Plagiarism Detection Tool
    </div>

    <strong>
      <span>Copyright &copy; 2018-{{ (new Date()).getFullYear() }} </span>
      <a href="https://trustsoft.xjtu.edu.cn">trustsoft.xjtu.edu.cn</a>
      <span>.</span>
    </strong>
    
    <span>
      All rights reserved.
    </span>
  </MainFooter>
</template>

<script>
import MainFooter from '@/components/admin-lte/MainFooter'

export default {
  name: 'TheMainFooter',

  components: {
    MainFooter,
  },
}
</script>
