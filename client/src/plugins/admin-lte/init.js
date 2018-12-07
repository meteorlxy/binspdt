// Manually trigger admin-lte scripts

export default function initAdminLTE() {
  // admin-lte/build/js/Layout.js
  $(window).trigger('load')
  
  // admin-lte/build/js/Treeview.js
  $(window).trigger('resize')
}
