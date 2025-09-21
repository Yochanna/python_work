from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Project,Screenshot
from .forms import ProjectForm,ScreenshotForm
class ProjectList(ListView):
    model=Project; paginate_by=10
    def get_queryset(self):
        qs=super().get_queryset()
        q=self.request.GET.get("q","").strip()
        status=self.request.GET.get("status","").strip()
        if q: qs=qs.filter(title__icontains=q)
        if status: qs=qs.filter(status=status)
        return qs
class ProjectDetail(DetailView): model=Project
class ProjectCreate(CreateView): model=Project; form_class=ProjectForm; success_url=reverse_lazy("projects:list")
class ProjectUpdate(UpdateView): model=Project; form_class=ProjectForm; success_url=reverse_lazy("projects:list")
class ProjectDelete(DeleteView): model=Project; success_url=reverse_lazy("projects:list")
class ScreenshotCreate(CreateView): model=Screenshot; form_class=ScreenshotForm; success_url=reverse_lazy("projects:list")
class ScreenshotUpdate(UpdateView): model=Screenshot; form_class=ScreenshotForm; success_url=reverse_lazy("projects:list")
class ScreenshotDelete(DeleteView): model=Screenshot; success_url=reverse_lazy("projects:list")