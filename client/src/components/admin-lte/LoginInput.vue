<template>
  <div class="input-group mb-3">
    <input
      class="form-control"
      :class="{
        'is-valid': isValid,
        'is-invalid': isInvalid,
      }"
      :autocomplete="autocomplete"
      :disabled="disabled"
      :name="name"
      :placeholder="placeholder"
      :type="type"
      :value="value"
      @input="updateValue"
      @change="updateValue"
      @blur="$emit('blur')" 
      @focus="$emit('focus')">

    <div class="input-group-append">
      <span class="input-group-text">
        <FaIcon
          v-if="icon"
          :icon="icon" />
      </span>
    </div>

    <div
      v-if="feedbackValid"
      class="valid-feedback">
      {{ feedbackValid }}
    </div>

    <div
      v-if="feedbackInvalid"
      class="invalid-feedback">
      {{ feedbackInvalid }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginInput',

  props: {
    autocomplete: {
      type: Boolean,
      required: false,
      default: false,
    },

    disabled: {
      type: Boolean,
      required: false,
      default: false,
    },

    feedbackInvalid: {
      type: [String, Boolean],
      required: false,
      default: false,
    },

    feedbackValid: {
      type: [String, Boolean],
      required: false,
      default: false,
    },

    icon: {
      type: [String, Boolean, Array],
      required: false,
      default: false,
    },

    isInvalid: {
      type: Boolean,
      required: false,
      default: false,
    },

    isValid: {
      type: Boolean,
      required: false,
      default: false,
    },

    name: {
      type: String,
      required: false,
      default: '',
    },

    placeholder: {
      type: String,
      required: false,
      default: '',
    },

    type: {
      type: String,
      required: false,
      default: 'text',
    },

    value: {
      type: [String, Number],
      required: false,
      default: '',
    },
  },

  methods: {
    updateValue (e) {
      this.$emit('input', e.target.value)
    }
  },
}
</script>

