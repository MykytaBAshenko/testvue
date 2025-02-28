<script setup>
import { ref, onMounted } from 'vue';
const { $api } = useNuxtApp();

const locations = ref([]);

// Fetch locations and assign to the `locations` variable
const fetchLocations = async () => {
  try {
    const response = await $api.getLocations();
    locations.value = response; // Now locations.value will hold the plain array
  } catch (error) {
    console.error('Error fetching locations:', error);
  }
};

// Call `fetchLocations` when the component is mounted
onMounted(fetchLocations);
// Delete location and re-fetch the list after a successful delete
const deleteLocation = async (locationId) => {
  try {
    deleteId.value=locationId;
    await $api.deleteLocation(locationId); // Delete the location
    console.log(`Location ${locationId} deleted.`);
    fetchLocations(); // Re-fetch the locations list
  } catch (error) {
    console.error('Error deleting location:', error);
  }
};

const createLocation = async (name) => {
  try {
    await $api.createLocation(name); // Delete the location
    console.log(`Location ${name} created.`);
    fetchLocations(); // Re-fetch the locations list
  } catch (error) {
    console.error('Error deleting location:', error);
  }
};
const deleteId = ref(-1); // This controls the visibility of LocationPopup
const popupVisibility = ref(false); // This controls the visibility of LocationPopup
const sidebarVisibility = ref(false); // This controls the visibility of LocationPopup
const forecastData = ref({}); // This controls the visibility of LocationPopup
const forecastName = ref(""); // This controls the visibility of LocationPopup

const togglePopup = () => {
  popupVisibility.value = !popupVisibility.value;
};

const toggleSidebar = () => {
  sidebarVisibility.value = !sidebarVisibility.value;
};

const startForecast = async (id, name) => {
  if (deleteId.value === id) {
    return
  }
  let forecastOut = toRaw(await $api.forecast(id)); // Delete the location
  forecastData.value = forecastOut;
  forecastName.value = name;
  toggleSidebar();
}
</script>

<template>
    <Header />
    <TabelHeader :togglePopup="togglePopup"/>
    <TabelBody :startForecast="startForecast" :deleteLocation="deleteLocation" :locations="locations"/>
    <LocationPopup v-if="popupVisibility" :togglePopup="togglePopup"  :createLocation="createLocation"/>
    <Sidebar v-if="sidebarVisibility" :toggleSidebar="toggleSidebar" :forecastData="forecastData" :forecastName="forecastName"/>

</template>
<style>
body {
    position: relative;
}
</style>