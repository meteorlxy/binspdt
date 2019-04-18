<template>
  <VCard>
    <VCardText>
      <VSubheader>References</VSubheader>

      <ul>
        <li
          v-for="(val, index) in references"
          :key="index"
        >
          <a
            :href="val.link"
            target="_blank"
          >
            {{ val.title }}
          </a>
        </li>
      </ul>
    </VCardText>
  </VCard>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'

@Component
export default class WikiKeyReadWrite extends Vue {
  references: Array<{ title: string, link: string }> = [
    {
      title: 'None',
      link: '',
    },
  ]
}
</script>
