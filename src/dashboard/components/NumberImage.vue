<template>
    <div class="svg-container" v-html="getSvgComponent"></div>
  </template>
  
  <script setup>
  import { computed } from 'vue';
  
  // Import SVG files as raw text
  import Sun from '~/assets/icons/1.svg?raw';
  import Storm from '~/assets/icons/2.svg?raw';
  import MidCloud from '~/assets/icons/3.svg?raw';
  import Cloud from '~/assets/icons/4.svg?raw';
  import MidRain from '~/assets/icons/5.svg?raw';
  
  const props = defineProps({
    numberImage: Number // The number input
  });
  
  // Choose which SVG to display based on the number
  const getSvgComponent = computed(() => {
    if (props.numberImage < 3) return Sun;
    if (props.numberImage < 6) return MidCloud;
    if (props.numberImage < 12) return Cloud;
    if (props.numberImage < 20) return MidRain;
    return Storm;
  });
  </script>
  
  <style scoped>
  .svg-container {
    width: 100%;
    max-width: 300px;
  }
  </style>