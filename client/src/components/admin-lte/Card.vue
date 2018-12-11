<template>
  <div
    v-if="!isRemoved"
    class="card"
    :class="cardClass">
    <slot name="header">
      <CardHeader>
        <CardTitle slot="title">
          <slot name="title"/>
        </CardTitle>

        <slot name="tools">
          <CardTools v-if="tools">
            <button
              v-if="dismissible"
              class="btn btn-tool"
              @click="isRemoved = true">
              <FaIcon icon="times"/>
            </button>

            <button
              v-if="collapsed"
              class="btn btn-tool"
              @click="isCollapsed = !isCollapsed">
              <FaIcon icon="times"/>
            </button>
          </CardTools>
        </slot>
      </CardHeader>
    </slot>

    <slot name="body">
      <div class="card-body p-0">
        <slot name="default"/>
      </div>
    </slot>

    <slot name="footer"/>
  </div>
</template>

<script>
import CardHeader from './CardHeader.vue'
import CardTitle from './CardTitle.vue'
import CardTools from './CardTools.vue'

export default {
  name: 'Card',

  components: {
    CardHeader,
    CardTitle,
    CardTools,
  },

  props: {
    collapsed: {
      type: Boolean,
      required: false,
      default: false,
    },

    collapsible: {
      type: Boolean,
      required: false,
      default: false,
    },

    dismissible: {
      type: Boolean,
      required: false,
      default: false,
    },

    tools: {
      type: Boolean,
      required: false,
      default: false,
    },

    type: {
      type: String,
      required: false,
      default: 'default',
      validator: (val) => ['default', 'info', 'success', 'warning', 'danger'].includes(val),
    },

    outline: {
      type: Boolean,
      required: false,
      default: false,
    },
  },

  data () {
    return {
      isCollapsed: this.collapsed,
      isRemoved: false,
    }
  },

  computed: {
    cardClass () {
      return [
        {
          'collapsed-card': this.isCollapsed,
          'card-outlin': this.outline,
        },
        `card-${this.type}`,
      ]
    }
  },
}
</script>

