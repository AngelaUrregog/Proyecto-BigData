<script>
    function listarUsuarios() {
        // Mostrar el indicador de carga
        document.getElementById('div_cargando').style.display = 'block';
        
        fetch('/listar-usuarios')
            .then(response => response.json())
            .then(data => {
                const tablaUsuarios = document.getElementById('tbodyUsuarios'); 
                const contenedor = document.getElementById('listadoUsuarios'); 
                
                tablaUsuarios.innerHTML = '';
                
                if (data.length === 0) {
                    const row = document.createElement('tr');
                    row.innerHTML = '<td colspan="6" class="text-center">No hay usuarios registrados</td>';
                    tablaUsuarios.appendChild(row);
                } else {
                    data.forEach(usuario => {
                        const row = document.createElement('tr');
                        const permisos = usuario.permisos || {};
                        
                        
                        const mostrarPermiso = (valor) => {
                            if (valor === true || valor === 'true') {
                                return '<span class="badge bg-success">Sí</span>';
                            } else {
                                return '<span class="badge bg-secondary">No</span>';
                            }
                        };
                        
                        row.innerHTML = `
                            <td>${usuario.usuario || ''}</td>
                            <td>${usuario.password || ''}</td>
                            <td>${mostrarPermiso(permisos.login)}</td>
                            <td>${mostrarPermiso(permisos.admin_usuarios)}</td>
                            <td>${mostrarPermiso(permisos.admin_elastic)}</td>
                            <td>${mostrarPermiso(permisos.admin_data_elastic)}</td>
                        `;
                        tablaUsuarios.appendChild(row);
                    });
                }
                
                document.getElementById('div_cargando').style.display = 'none';
                contenedor.style.display = 'block';
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error al obtener la lista de usuarios');
                document.getElementById('div_cargando').style.display = 'none';
            });
    }
</script>
