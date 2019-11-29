import "@mdi/font/css/materialdesignicons.css";
import Vue from "vue";
import Vuetify, {
  VApp,
  VBtn,
  VSnackbar,
  VContainer,
  VLayout,
  VFlex,
  VSelect,
  VRadioGroup,
  VRadio,
  VIcon,
  VDialog,
  VCard,
  VCardTitle,
  VCardText,
  VCardActions,
  VCombobox,
  VDivider,
  VSpacer,
  VDataTable,
  VProgressCircular,
  VSwitch,
  VForm,
  VAutocomplete,
  VList,
  VListItem,
  VListItemTitle,
  VExpansionPanels,
  VExpansionPanel,
  VExpansionPanelHeader,
  VExpansionPanelContent,
  VMenu,
  VNavigationDrawer,
  VRow,
  VCol,
  VTabs,
  VTab,
  VTabsItems,
  VTabItem
} from "vuetify/lib";

Vue.use(Vuetify, {
  components: {
    VApp,
    VBtn,
    VSnackbar,
    VContainer,
    VLayout,
    VFlex,
    VSelect,
    VRadioGroup,
    VRadio,
    VIcon,
    VDialog,
    VCard,
    VCardTitle,
    VCardText,
    VCardActions,
    VCombobox,
    VDivider,
    VSpacer,
    VDataTable,
    VProgressCircular,
    VSwitch,
    VForm,
    VAutocomplete,
    VList,
    VListItem,
    VListItemTitle,
    VExpansionPanels,
    VExpansionPanel,
    VExpansionPanelHeader,
    VExpansionPanelContent,
    VMenu,
    VNavigationDrawer,
    VRow,
    VCol,
    VTabs,
    VTab,
    VTabsItems,
    VTabItem
  },
  iconfont: "mdi"
});

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: "#3f51b5",
        secondary: "#fcb902",
        third: "#00ace8",
        "header-primary": "#28669a",
        "light-blue": "#00ace8",
        "body-color": "#94979a"
      },
      dark: {
        primary: "#3f51b5",
        secondary: "#fcb902",
        third: "#00ace8",
        "header-primary": "#28669a",
        "light-blue": "#00ace8",
        "body-color": "#94979a"
      }
    }
  }
});
