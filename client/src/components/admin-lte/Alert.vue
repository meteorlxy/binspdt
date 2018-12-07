<template>
  <div
    class="alert"
    :class="className">
    <button
      v-if="dismissible"
      type="button"
      class="close"
      data-dismiss="alert"
      @click="$emit('close')">
      &times;
    </button>

    <h5>
      <FaIcon
        v-if="icon"
        class="mr-1"
        :icon="iconName"
        fixed-width />

      <slot name="title" />
    </h5>

    <slot name="text" />
  </div>
</template>

<script>
export default {
  name: 'Alert',

  props: {
    dismissible: {
      type: Boolean,
      required: false,
      default: true,
    },

    icon: {
      type: [String, Boolean, Array],
      required: false,
      default: true,
    },

    type: {
      type: String,
      required: false,
      default: 'info',
      validator: value => ['info', 'success', 'warning', 'danger'].includes(value),
    },
  },

  computed: {
    className () {
      return [
        {
          'alert-dismissible': this.dismissible,
        },
        `alert-${this.type}`,
      ]
    },

    iconName () {
      const typeIcon = {
        'info': 'info',
        'success': 'check',
        'warning': 'exclamation-triangle',
        'danger': 'ban',
      }
      return this.icon === true ? typeIcon[this.type] : this.type
    },
  },
}
</script>
