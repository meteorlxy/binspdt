<template>
  <ElForm>
    <ElFormItem :label="$t('binary.modules.select.module_1')">
      <ElSelect
        clearable
        :loading="loading"
        :placeholder="$t('binary.modules.select.module_1_placeholder')"
        v-model="result[0]">
        <template v-for="mod in modules">
          <ElOption
            v-if="mod.id != result[1]"
            :key="mod.id"
            :label="`[${mod.id}] ${mod.name}`"
            :value="mod.id">
          </ElOption>
        </template>
      </ElSelect>
    </ElFormItem>

    <ElFormItem :label="$t('binary.modules.select.module_2')">
      <ElSelect
        clearable
        :loading="loading"
        :placeholder="$t('binary.modules.select.module_2_placeholder')"
        v-model="result[1]">
        <template v-for="mod in modules">
          <ElOption
            v-if="mod.id != result[0]"
            :key="mod.id"
            :label="`[${mod.id}] ${mod.name}`"
            :value="mod.id">
          </ElOption>
        </template>
      </ElSelect>
    </ElFormItem>
  </ElForm>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name: 'ModuleSelect',
  data () {
    return {
      result: ['', '']
    }
  },
  computed: {
    ...mapState('binary/modules', [
      'modules',
      'loading'
    ]),
    selected () {
      return this.result[0] !== '' && this.result[1] !== ''
    }
  },
  watch: {
    result: {
      deep: true,
      handler () {
        this.emitResult()
      }
    }
  },
  created () {
    this.emitResult()
  },
  methods: {
    emitResult () {
      if (this.selected) {
        this.$emit('input', this.result)
      } else {
        this.$emit('input', null)
      }
    }
  }
}
</script>
