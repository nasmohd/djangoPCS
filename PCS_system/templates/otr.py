{% for i in roles %}
  {{ i }} {{ dicti.administrator }}
    {% for j in all_permission %}
      {% if dicti.i == j.permission_name %}
        <div class="checkbox">
      <label>
        <span> Yup </span>
        {{ j.permission_name }}
      </label>
      </div>
      {% endif %}

      {% if dicti.i != j.permission_name %}
      <div class="checkbox">
      <label>
        <span> No </span>
        {{ j.permission_name }}
      </label>
      </div>
      {% endif %}
    {% endfor %}
    <br/>
  {% endfor %}
  {% if i.role_id.role_type in all_permission %}
                      <div class="checkbox">
                      <label>
                        <input type="checkbox" name="{{ i.id }}" value="{{ i.permission_name }}" checked>

                        {{ i.permission_name }}
                      </label>
                      </div>
                      {% endif %}

                      {% if i.role_id.role_type not in all_permission %}
                      <div class="checkbox">
                      <label>
                        <input type="checkbox" name="{{ i.id }}" value="{{ i.permission_name }}">

                        {{ i.permission_name }}
                      </label>
                      </div>
                      {% endif %}

<div class="col-sm-4">
                    {% for i in all_permission %} 
                    <!-- #all_permission = <QuerySet [<Permission: 1, dashboard>, <Permission: 2, add user>, <Permission: 3, add project>]> -->
                      {% if i.role_id.role_type in all_permission %}
                      <div class="checkbox">
                      <label>
                        <input type="checkbox" name="{{ i.id }}" value="{{ i.permission_name }}" checked>

                        {{ i.permission_name }}
                      </label>
                      </div>
                      {% endif %}

                      {% if i.role_id.role_type not in all_permission %}
                      <div class="checkbox">
                      <label>
                        <input type="checkbox" name="{{ i.id }}" value="{{ i.permission_name }}">

                        {{ i.permission_name }}
                      </label>
                      </div>
                      {% endif %}
                    {% endfor %}

                  </div>