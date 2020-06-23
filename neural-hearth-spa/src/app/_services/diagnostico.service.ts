import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Result } from '../_models/result';

@Injectable({
  providedIn: 'root'
})
export class DiagnosticoService {
  baseUrl = environment.apiUrl;
  constructor(private http: HttpClient) { }

  getdiagnostico(): Observable<Result[]> {
    return this.http.get<Result[]>(this.baseUrl + 'Prediccion');
  }

  postPaciente(paciente: any) {
    return this.http.post(this.baseUrl + 'Prediccion', paciente);
  }

}
