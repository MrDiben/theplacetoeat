<template>
  <VContainer fluid class="main-content">
    <slot name="main-content"> </slot>
  </VContainer>
</template>

<script>
export default {
  name: "BaseContent",
  data() {
    return {};
  }
};
</script>

<style lang="scss">
.main-content {
  height: 100%;
}
</style>
