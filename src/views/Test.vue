<template>
  <h1>Therichpost.com</h1>

  <table class="table table-hover table-bordered" id="example">
    <thead>
      <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Email</th>
        <th>Job Title</th>
      </tr>
    </thead>
    <tbody>
      <td>d</td>
      <td>d</td>
      <td>d</td>
      <td>s</td>
      <!--
      <tr v-for="user in users" :key="user.id">
        <td>{{ user.id }}</td>
        <td>{{ user.name }}</td>
        <td>{{ user.email }}</td>
        <td>{{ user.job_title }}</td>
      </tr>
    --></tbody>
  </table>
</template>

<script>
import "bootstrap/dist/css/bootstrap.min.css";
import "jquery/dist/jquery.min.js";
import "datatables.net-dt/js/dataTables.dataTables";
import "datatables.net-dt/css/jquery.dataTables.min.css";
import $ from "jquery";

//import axios from "axios";
export default {
  mounted() {
    //API Call
    var table = $("#example").DataTable({
      //ajax: "https://datatables.net/examples/ajax/data/arrays.txt?_=1645705512738",
      columnDefs: [
        {
          targets: -1,
          data: null,
          defaultContent: "<button>Click!</button>",
        },
      ],
    });

    $("#example tbody").on("click", "button", function () {
      var data = table.row($(this).parents("tr")).data();
      alert(data[0] + "'s salary is: " + data[5]);
    });
  },
  data: function () {
    return {
      users: ["123"],
    };
  },
};
</script>