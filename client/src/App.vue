<template>
  <section class="container">
    <nav class="navbar px-4 navbar-dark bg-primary fixed-top">
      <span class="navbar-brand">
        Bhavcopy
      </span>
      <a href="https://github.com/allenabraham777/zerodha-equity-publisher" class="btn btn-outline-light ml-auto"
        ><i class="fa fa-github" aria-hidden="true"></i
      ></a>
    </nav>
    <div v-if="loading" class="mt-5 pt-5 text-center">
      <div class="spinner-grow text-primary" style="margin-top: 100px;" role="status">
        <span class="sr-only">Loading...</span>
      </div>
    </div>
    <div v-else class="mt-5 pt-5">
      <h4 v-if="lastUpdated" class="text-center text-decoration-underline">
        Bhavcopy for the date {{ lastUpdated }}
      </h4>
      <div
        class="row w-100 mt-5 p-2 border border-outlined"
        style="--bs-gutter-x: 0"
      >
        <div class="col-md-8">
          <a
            v-if="equities && equities.length"
            :href="'/api/equities/export/' + name"
            class="btn btn-outline-dark"
            >Export as CSV <i class="fa fa-download"></i
          ></a>
        </div>
        <form class="col-md-4" @submit="search">
          <div class="input-group">
            <input
              class="form-control"
              style="margin-right: 0.3rem"
              placeholder="Search by company name"
              @change="changeName"
            />
            <div class="input-group-append">
              <button class="input-group-text btn btn-success">
                <i class="fa fa-search" aria-hidden="true"></i>
              </button>
            </div>
          </div>
        </form>
      </div>
      <Body v-bind:equities="equities" />
    </div>
    <div class="text-center text-secondary">
      <p>
        *Data updates everyday at 18:00 PM IST (UTC +05:30)
      </p>
    </div>
  </section>
</template>

<script>
import Body from "./components/Body.vue";
import { fetchAllEquities, fetchEquitiesByName } from "./utils/api";

export default {
  name: "App",
  components: {
    Body,
  },
  data() {
    return {
      loading: true,
      equities: [],
      lastUpdated: "",
      name: "",
    };
  },
  methods: {
    changeName({ target: { value } }) {
      this.name = value;
      if (!value) this.loadEquities();
    },
    async search(e) {
      e.preventDefault();
      this.loading = true;
      this.equities = await fetchEquitiesByName(this.name);
      this.loading = false;
    },
    async loadEquities() {
      // this.loading = true;
      const { equities, lastUpdated } = await fetchAllEquities();
      this.equities = equities;
      this.lastUpdated = lastUpdated;
      this.loading = false;
    },
  },
  mounted() {
    this.loadEquities();
  },
};
</script>

<style></style>
