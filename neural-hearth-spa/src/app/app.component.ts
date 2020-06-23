import { Component, OnInit } from '@angular/core';
import { Pacient } from './_models/pacient';
import { Result } from './_models/result';
import { DiagnosticoService } from './_services/diagnostico.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  result: Result;
  pacient: any = {};
  genderList = [{value: 0, display: 'Hombre'}, {value: 1, display: 'Mujer'}];
  visibleForm = true;

  constructor(private diagnosticoService: DiagnosticoService) {}


  ngOnInit(): void {

  }

  enviarDatosPacientes(){
    this.diagnosticoService.postPaciente(this.pacient).subscribe(next => {
      console.log('todo bien');
      this.loadDiagnostico();
      this.toggleVisibleForm();
    }, error => {
        console.log('error');
    });
  }

  loadDiagnostico(){
      this.diagnosticoService.getdiagnostico().subscribe((response) => {
      this.result = response[0];
      console.log(this.result);
      console.log('todo kul');
      }, error => {
        console.log('Error');
      });
  }

  toggleVisibleForm()
  {
    this.visibleForm = !this.visibleForm;
  }

}
