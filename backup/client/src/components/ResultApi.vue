<template>
  <div v-if="result">
    <h3>{{ $t('binary.analysis.api.result.title') }}</h3>

    <table class="el-table">
      <th>
        <td>{{ result.module_1.name }}</td>
        <td>2</td>
      </th>
    </table>
  </div>
</template>

<script>
export default {
  name: 'ResultApi',
  props: {
    result: {
      type: [Object, null],
      required: false,
      default: null
    }
  }
}
</script>
