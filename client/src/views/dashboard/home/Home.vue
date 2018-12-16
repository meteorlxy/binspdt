<template>
  <VLayout>
    <VFlex xs12>
      <VCard>
        <VCardTitle class="pa-4">
          <div>
            <div class="headline">
              Welcome to BinSPDT
            </div>
            <div class="grey--text">
              Binary Software Plagiarism Detection Tool
            </div>
          </div>
        </VCardTitle>

        <VCardText>
          <VSubheader>There is nothing here this page</VSubheader>
        </VCardText>
      </VCard>
    </VFlex>
  </VLayout>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'

@Component
export default class DashboardHome extends Vue {
}
</script>
