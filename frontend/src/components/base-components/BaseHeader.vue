<template>
  <VContainer class="main-header">
    <VRow>
      <VCol cols="12" class="display-1">
        <h1><slot name="title"></slot></h1>
      </VCol>
    </VRow>
  </VContainer>
</template>

<script>
export default {
  name: "BaseHeader",
  data() {
    return {};
  }
};
</script>

<style lang="scss">
.main-header {
  min-height: 15%;
}
</style>
