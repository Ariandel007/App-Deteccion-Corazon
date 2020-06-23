/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { DiagnosticoService } from './diagnostico.service';

describe('Service: Diagnostico', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [DiagnosticoService]
    });
  });

  it('should ...', inject([DiagnosticoService], (service: DiagnosticoService) => {
    expect(service).toBeTruthy();
  }));
});
