<template>
    <header>
        Weather app
    </header>
  </template>
  
  <script setup>
  defineProps({
    title: String,
    message: String,
  });
  </script>
  
  <style scoped>
    header {
        text-align: center;
        font-size: 40px;
        font-weight: 700;
        color: white;
    }
  </style>