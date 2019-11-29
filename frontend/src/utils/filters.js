import Vue from "vue";

Vue.filter(
  "truncate",
  (text, stop, clamp) =>
    text.slice(0, stop) + (stop < text.length ? clamp || "..." : "")
);

Vue.filter("lowercase", value => {
  if (value) {
    value = value.toString();
    return value.toLowerCase();
  }
});

Vue.filter("badgeName", value => {
  if (value) {
    value = value[0];
    return value.toUpperCase();
  }
});
