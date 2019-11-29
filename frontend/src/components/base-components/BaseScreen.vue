<template>
  <VContainer>
    <BaseContent>
      <template v-slot:main-content><slot name="main-content"></slot></template>
    </BaseContent>
  </VContainer>
</template>

<script>
export default {
  name: "BaseScreen",
  data() {
    return {};
  }
};
</script>

<style style="scss">
.main-content {
  height: 100%;
}
</style>
