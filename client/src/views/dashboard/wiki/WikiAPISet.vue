<template>
  <VCard>
    <VCardText>
      <VSubheader>References</VSubheader>

      <ul>
        <li
          v-for="(val, index) in references"
          :key="index">
          <a
            :href="val.link"
            target="_blank">
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
export default class WikiAPISet extends Vue {
  references: Array<{ title: string, link: string }> = [
    {
      title: 'A static API birthmark for Windows binary executables',
      link: 'https://ac.els-cdn.com/S0164121208002689/1-s2.0-S0164121208002689-main.pdf?_tid=0fe710a3-273f-43ba-9e23-f00a67e04362&acdnat=1544781101_6354108a271317802a4ba24798396bfc',
    },
  ]
}
</script>
