<template>
    <div class="tabelHeaderShell">
        <div class="tabelHeader">
    
            <div>
                Locations
            </div>
            <button @click="togglePopup()">
                + Add Location
            </button>
        </div>
    </div>
  </template>
  
  <script setup>
  defineProps({
    togglePopup: Function
  });
  </script>
  
  <style scoped>
    .tabelHeaderShell {
        display: grid;
        align-items: center;
        justify-items: center;
        width: 100%;
        padding: 50px 50px 10px;
    }
    .tabelHeader {
        display: grid;
        width: 100%;
        max-width: 1280px;
        align-items: center;
        grid-template-columns: 1fr 1fr;
    }
    .tabelHeader div{
        font-weight: 700;
        font-size: 40px;
    }
    .tabelHeader button{
        background-color: white;
        color: black;
        padding:10px 25px;
        border: none;
        border-radius: 6px;
        justify-self: end;
    }
  </style>